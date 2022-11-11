from typing import List

import discord
from discord import Intents, Message
from discord.ext.commands import Bot

from main.constants import rel_id
from main.string_resources import StringResources


class RelBot(Bot):

    def __init__(self, extension_list: List[str], token: str) -> None:
        super().__init__(command_prefix="rel", description=StringResources.bot_description, intents=Intents.all())
        self.token = token
        self.extension_list = extension_list
        self.rel = None

    async def on_message(self, message: Message, /) -> None:
        return await super().on_message(message)

    def run(self):
        return super().run(self.token)

    async def setup_hook(self) -> None:
        for extension in self.extension_list:
            await self.load_extension(extension)
        self.tree.copy_global_to(guild=discord.Object(rel_id))
        await self.tree.sync(guild=discord.Object(rel_id))
