from typing import Any, Optional

import discord
from discord import Interaction

import main.constants


class Dropdown(discord.ui.Select):
    def __init__(self, callback):
        self.passed_callback = callback

        options = [
            discord.SelectOption(label='Fluency Level'),
            discord.SelectOption(label='Colors'),
            discord.SelectOption(label='Native Language'),
            discord.SelectOption(label='Other')
        ]

        super().__init__(placeholder='', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)


class Button(discord.ui.Button):
    def __init__(self, label, callback, emoji=None):
        super().__init__(label=label, emoji=emoji)
        self.passed_callback = callback

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)


class RolesView(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.selected_role = None
        self.dropdown = Dropdown(self.on_dropdown_select)
        self.buttons = []
        self.add_item(self.dropdown)

    async def on_dropdown_select(self, dropdown: Dropdown, interaction: Interaction):
        self.clear_items()
        values = dropdown.values
        self.buttons.clear()

        if values[0] == 'Fluency Level':
            self.buttons.append(Button("Native", self.on_button_click))
            self.buttons.append(Button("Advanced", self.on_button_click))
            self.buttons.append(Button("Intermediate", self.on_button_click))
            self.buttons.append(Button("Beginner", self.on_button_click))
        elif values[0] == 'Colors':
            for color in main.constants.supported_colors:
                self.buttons.append(Button(color.name, self.on_button_click, emoji=color.emoji))
        elif values[0] == 'Native Language':
            for each in main.constants.supported_languages:
                self.buttons.append(Button(each, self.on_button_click))

        for button in self.buttons:
            self.add_item(button)

        await interaction.response.edit_message(content="Click on the button for the role you want:", view=self)

    async def on_button_click(self, button: Button, interaction: Interaction):
        self.selected_role = button.label
        self.clear_items()
        await interaction.response.edit_message(content="Role added, you can now dismiss this message!", view=self)
