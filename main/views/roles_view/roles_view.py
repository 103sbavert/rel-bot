from typing import List

import discord
from discord import Interaction

from main.constants import roles_categories, fluency_levels, misc_roles, pronoun_roles
from main.views.view_components.buttons import FluencyLevelButton, MiscRoleButton, PageChangeButton, PronounRoleButton
from main.views.view_components.dropdowns import RolesCategoryDropdown, NativeLanguagesDropdown

# Creates subclass for viewing the role buttons
class RolesView(discord.ui.View):

    # Creates buttons and dropdown menus for the /roles command
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

    def misc_role_buttons(self):
        buttons = []
        for misc_role in misc_roles:
            button = MiscRoleButton(misc_role, self.on_miscrole_button_click)
            buttons.append(button)
        return buttons
    
    def pronoun_role_buttons(self):
        buttons = []
        for pronoun_role in pronoun_roles:
            button = PronounRoleButton(pronoun_role, self.on_pronoun_button_click)
            buttons.append(button)
        return buttons

    def page_change_buttons(self):
        return [
            PageChangeButton(PageChangeButton.PageChangeButtonType.prev_page, self.on_pagechange_button_click),
            PageChangeButton(PageChangeButton.PageChangeButtonType.next_page, self.on_pagechange_button_click)
        ]

    # Code to be executed when choosing a category on the role category dropdown menu
    async def on_rolescategory_dropdown_select(self, dropdown: RolesCategoryDropdown, interaction: Interaction):
        self.clear_items()
        selection = dropdown.values[0]
        # Displays respective menu depending on the role category chosen
        if selection == roles_categories[0].code:
            buttons = self.fluency_level_buttons()
            for button in buttons:
                self.add_item(button)
            await interaction.response.edit_message(content="What is your fluency level in English? If you aren't sure, choose Intermediate.", view=self)
        elif selection == roles_categories[1].code:
            self.nativelanguages_dropdown = NativeLanguagesDropdown(self.on_nativelanguages_dropdown_select)
            self.add_item(self.nativelanguages_dropdown)
            for button in self.page_change_buttons():
                self.pagechange_buttons.append(button)
                self.add_item(button)
            await interaction.response.edit_message(content="Select your native language...", view=self)
        elif selection == roles_categories[2].code:
            buttons = self.misc_role_buttons()
            for button in buttons:
                self.add_item(button)
            await interaction.response.edit_message(content="Select other roles...", view=self)
        elif selection == roles_categories[3].code:
            buttons = self.pronoun_role_buttons()
            for button in buttons:
                self.add_item(button)
            await interaction.response.edit_message(content="Select pronoun roles...", view=self)
            
    # Code to be executed when choosing a native language on the native language dropdown menu
    async def on_nativelanguages_dropdown_select(self, dropdown: NativeLanguagesDropdown, interaction: Interaction):
        self.clear_items()
        for value in dropdown.values:
            role = interaction.guild.get_role(int(value))
            await interaction.user.add_roles(role)

        await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)
        
    # Code to be executed when choosing a role on the misc role menu
    async def on_miscrole_button_click(self, button: MiscRoleButton, interaction: Interaction):
        self.clear_items()
        interaction_user = interaction.user
        requested_role = interaction.guild.get_role(button.role_id)
        user_has_requested_role = interaction_user.get_role(requested_role.id) is not None
        if user_has_requested_role:
            await interaction_user.remove_roles(requested_role)
            await interaction.response.edit_message(content="Role removed! You can now dismiss this message.", view=self)
        else:
            await interaction_user.add_roles(requested_role)
            await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)
            
    # Code to be executed when choosing a role on the pronoun role menu     
    async def on_pronoun_button_click(self, button: MiscRoleButton, interaction: Interaction):
        self.clear_items()
        interaction_user = interaction.user
        requested_role = interaction.guild.get_role(button.role_id)
        user_has_requested_role = interaction_user.get_role(requested_role.id) is not None
        if user_has_requested_role:
            await interaction_user.remove_roles(requested_role)
            await interaction.response.edit_message(content="Role removed! You can now dismiss this message.", view=self)
        else:
            await interaction_user.add_roles(requested_role)
            await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)
    
    # Code to be executed when choosing a role on the fluency level menu   
    async def on_fluencylevel_button_click(self, button: FluencyLevelButton, interaction: Interaction):
        self.clear_items()
        interaction_user = interaction.user
        requested_role = interaction.guild.get_role(button.role_id)
        user_has_requested_role = interaction_user.get_role(requested_role.id) is not None

        # Clears any previously assigned fluency level roles from the user 
        # This prevents them having two fluency level roles
        async def clear_roles():
            await interaction_user.remove_roles(
                discord.Object(fluency_levels[0].role_id),
                discord.Object(fluency_levels[1].role_id),
                discord.Object(fluency_levels[2].role_id),
                discord.Object(fluency_levels[3].role_id)
            )

        await clear_roles()
        # Assigns requested role to the user and sends a confirmation message
        if user_has_requested_role:
            await interaction.response.edit_message(content="Role removed! You can now dismiss this message.", view=self)
        else:
            await interaction_user.add_roles(requested_role)
            await interaction.response.edit_message(content="Role added! You can now dismiss this message.", view=self)

    # Code to be executed when a page change button is clicked
    # Goes to the next or previous page
    async def on_pagechange_button_click(self, button: PageChangeButton, interaction: Interaction):
        if button.label == "Next Page":
            self.nativelanguages_dropdown.next_page()
        elif button.label == "Prev Page":
            self.nativelanguages_dropdown.prev_page()
        # Displays the next or previous page
        self.refresh_page_change_buttons(self.nativelanguages_dropdown.slice_start, self.nativelanguages_dropdown.slice_end)
        await interaction.response.edit_message(content="Select your native language...", view=self)
        
    # Refreshes the menu depending on the page selected
    def refresh_page_change_buttons(self, slice_start: int, slice_end: int):
        for button in self.pagechange_buttons:
            button.refresh(slice_start, slice_end)
