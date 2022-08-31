import os
from typing import List

import discord
from discord import Intents
from discord.ext.commands import Bot

from main.constants import rel_id, role_channels
from main.views.levels_view.levels_view import LevelsView

FLUENCY_MESSAGE_ID_KEY = "fluency_message_id"
LANGUAGES_MESSAGE_ID_KEY = "languages_message_id"
MISC_MESSAGE_ID_KEY = "misc_message_id"


class RelBot(Bot):
    DESCRIPTION = """A simple bot made with discord.py V2 for the r/EnglishLearning Discord server"""

    def __init__(self, extension_list: List[str], token: str) -> None:
        super().__init__(command_prefix="rel", description=RelBot.DESCRIPTION, intents=Intents.all())
        self.token = token
        self.extension_list = extension_list
        self.rel = None

    async def on_ready(self):
        self.rel = discord.utils.get(self.guilds, id=rel_id)
        levels_channel = discord.utils.get(self.rel.channels, id=role_channels[0])
        fluency_message_id = os.getenv(FLUENCY_MESSAGE_ID_KEY)
        if fluency_message_id is not None:
            message = levels_channel.get_partial_message(int(fluency_message_id))
            await message.edit(view=LevelsView())
        else:
            fluency_message = await levels_channel.send(content="What is your fluency level in English? If you aren't sure, choose Intermediate.", view=LevelsView())
            os.putenv(FLUENCY_MESSAGE_ID_KEY, str(fluency_message.id))

    def run(self):
        return super().run(self.token)

    async def setup_hook(self) -> None:
        for extension in self.extension_list:
            await self.load_extension(extension)
        await self.tree.sync(guild=discord.Object(rel_id))

