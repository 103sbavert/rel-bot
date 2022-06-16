import enum
from typing import Any

from discord import ButtonStyle, Interaction
from discord.ui import Button

from main.constants import supported_languages


class FluencyLevelButton(Button):

    def __init__(self, role, callback):
        super().__init__(label=role.label, style=ButtonStyle.primary)
        self.role_id = role.role_id
        self.passed_callback = callback

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)


class MiscRoleButton(Button):

    def __init__(self, role, callback):
        super().__init__(label=role.label, style=ButtonStyle.primary)
        self.role_id = role.role_id
        self.passed_callback = callback

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)


class PageChangeButton(Button):
    class PageChangeButtonType(enum.IntEnum):
        prev_page = 0
        next_page = 1

    def __init__(self, button_type: PageChangeButtonType, callback):
        label = "Next Page" if button_type == PageChangeButton.PageChangeButtonType.next_page else "Prev Page"
        super().__init__(label=label)
        self.button_type = button_type
        if self.button_type == PageChangeButton.PageChangeButtonType.prev_page:
            self.disabled = True
        self.passed_callback = callback

    async def callback(self, interaction: Interaction) -> Any:
        await self.passed_callback(self, interaction)

    def refresh(self, slice_start: int, slice_end: int):
        if self.button_type == PageChangeButton.PageChangeButtonType.next_page:
            if slice_end >= len(supported_languages) - 1:
                self.disabled = True
            else:
                self.disabled = False
        if self.button_type == PageChangeButton.PageChangeButtonType.prev_page:
            if slice_start <= 0:
                self.disabled = True
            else:
                self.disabled = False
