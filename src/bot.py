import os
import json
import nextcord
from nextcord.ext import commands


class RelBot(commands.Bot):

    def __init__(self, command_prefix=None, help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command, description, **options)

    async def on_ready(self):
        await print(f'We have logged in as {self.user}')
