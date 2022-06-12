from typing import Type, Any

from discord import app_commands, Intents
from discord.ext import commands


class RelBot(commands.bot.Bot):
    DESCRIPTION = ""

    def __init__(self, token: str, *, tree_cls: Type[app_commands.CommandTree[Any]] = app_commands.CommandTree, **options: Any) -> None:
        super().__init__(None, help_command=None, tree_cls=tree_cls, description=RelBot.DESCRIPTION, intents=Intents.all(), **options)
        self.token = token

    def run(self):
        return super().run(self.token)

    async def setup_hook(self, *extensions: str) -> None:
        await super().setup_hook()
        for extension in extensions:
            await self.load_extension(extension)
        await self.tree.sync()
