from typing import List

import discord
from discord import Intents
from discord.ext.commands import Bot


class RelBot(Bot):
    DESCRIPTION = """A simple bot made with discord.py V2 for the r/EnglishLearning Discord server"""

    def __init__(self, extension_list: List[str], token: str, guild_ids: List[str]) -> None:
        super().__init__(command_prefix="rel", description=RelBot.DESCRIPTION, intents=Intents.all())
        self.token = token
        self.extension_list = extension_list
        self.guild_ids = guild_ids

    def run(self):
        return super().run(self.token)

    async def setup_hook(self) -> None:
        for extension in self.extension_list:
            await self.load_extension(extension)
        for guild_id in self.guild_ids:
            guild = discord.Object(guild_id)
            await self.tree.sync(guild=guild)
