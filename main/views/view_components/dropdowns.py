from typing import Any

from discord import Interaction, SelectOption
from discord.ui import Select

from main.constants import roles_categories, supported_languages

# Defines all the dropdown menus used by the bot 
class RolesCategoryDropdown(Select):
    def __init__(self, callback):
        self.passed_callback = callback
        options = []
        for category in roles_categories:
            options.append(SelectOption(label=category.label, value=category.code))
        super().__init__(placeholder="Choose a role category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)


class NativeLanguagesDropdown(Select):

    def __init__(self, callback):
        self.passed_callback = callback
        self.slice_start = 0
        self.slice_end = 25
        options = []
        for language in supported_languages[self.slice_start:self.slice_end]:
            options.append(SelectOption(label=language.label, value=language.role_id))
        super().__init__(placeholder="Pick your native language...", min_values=1, max_values=3, options=options)

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)

    def increment_slice(self):
        self.slice_start += 25
        self.slice_end += 25

    def decrement_slice(self):
        self.slice_start -= 25
        self.slice_end -= 25

    def next_page(self):
        self.options.clear()
        self.increment_slice()
        options = []
        for language in supported_languages[self.slice_start:self.slice_end]:
            options.append(SelectOption(label=language.label, value=language.role_id))
        self.options = options

    def prev_page(self):
        self.options.clear()
        self.decrement_slice()
        options = []
        for language in supported_languages[self.slice_start:self.slice_end]:
            options.append(SelectOption(label=language.label, value=language.role_id))
        self.options = options
