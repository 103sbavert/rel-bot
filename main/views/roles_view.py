from typing import List

import discord
from discord import Interaction

from main.constants import roles_categories, fluency_levels
from main.views.buttons import FluencyLevelButton, PageChangeButton
from main.views.dropdowns import RolesCategoryDropdown, NativeLanguagesDropdown


class RolesView(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.nativelanguages_dropdown = None
        self.pagechange_buttons: List[PageChangeButton] = []
        dropdown = RolesCategoryDropdown(self.on_rolescategory_dropdown_select)
        self.add_item(dropdown)

    def fluency_level_buttons(self):
        buttons = []
        for fluency_level in fluency_levels:
            button = FluencyLevelButton(fluency_level, self.on_fluencylevel_button_click)
            buttons.append(button)
        return buttons

    def page_change_buttons(self):
        return [
            PageChangeButton(PageChangeButton.PageChangeButtonType.prev_page, self.on_pagechange_button_click),
            PageChangeButton(PageChangeButton.PageChangeButtonType.next_page, self.on_pagechange_button_click)
        ]

    async def on_rolescategory_dropdown_select(self, dropdown: RolesCategoryDropdown, interaction: Interaction):
        self.clear_items()
        selection = dropdown.values[0]
        if selection == roles_categories[0].code:
            buttons = self.fluency_level_buttons()
            for button in buttons:
                self.add_item(button)
            await interaction.response.edit_message(content="Select your English fluency level...", view=self)
        elif selection == roles_categories[1].code:
            self.nativelanguages_dropdown = NativeLanguagesDropdown(self.on_nativelanguages_dropdown_select)
            self.add_item(self.nativelanguages_dropdown)
            for button in self.page_change_buttons():
                self.pagechange_buttons.append(button)
                self.add_item(button)
            await interaction.response.edit_message(content="Select your native language...", view=self)

    async def on_nativelanguages_dropdown_select(self, dropdown: NativeLanguagesDropdown, interaction: Interaction):
        self.clear_items()
        role = interaction.guild.get_role(int(dropdown.values[0]))
        await interaction.user.add_roles(role)
        await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)

    async def on_fluencylevel_button_click(self, button: FluencyLevelButton, interaction: Interaction):
        self.clear_items()
        interaction_user = interaction.user
        requested_role = interaction.guild.get_role(button.role_id)
        user_has_requested_role = interaction_user.get_role(requested_role.id) is not None

        async def clear_roles():
            await interaction_user.remove_roles(
                discord.Object(fluency_levels[0].role_id),
                discord.Object(fluency_levels[1].role_id),
                discord.Object(fluency_levels[2].role_id)
            )

        await clear_roles()
        if user_has_requested_role:
            await interaction_user.remove_roles(requested_role)
        else:
            await interaction_user.add_roles(requested_role)

        await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)

    async def on_pagechange_button_click(self, button: PageChangeButton, interaction: Interaction):
        if button.label == "Next Page":
            self.nativelanguages_dropdown.next_page()
        elif button.label == "Prev Page":
            self.nativelanguages_dropdown.prev_page()
        self.refresh_buttons(self.nativelanguages_dropdown.slice_start, self.nativelanguages_dropdown.slice_end)
        await interaction.response.edit_message(content="Select your native language...", view=self)

    def refresh_buttons(self, slice_start: int, slice_end: int):
        for button in self.pagechange_buttons:
            button.refresh(slice_start, slice_end)
