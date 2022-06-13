from typing import Type, Any, List
import discord
from discord import app_commands, Intents
from discord.ext import commands


class RelBot(commands.bot.Bot):
    DESCRIPTION = ""

    def __init__(self, extension_list: List[str], token: str, rel_id: str, *,
                 tree_cls: Type[app_commands.CommandTree[Any]] = app_commands.CommandTree, **options: Any) -> None:
        super().__init__("!", help_command=None, tree_cls=tree_cls,
                         description=RelBot.DESCRIPTION, intents=Intents.all(), **options)
        self.token = token
        self.rel_id = rel_id
        self.extension_list = extension_list
        self.guild = discord.Object(id=rel_id)

    def run(self):
        return super().run(self.token)

    async def setup_hook(self) -> None:
        for extension in self.extension_list:
            await self.load_extension(extension)

        # self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)
