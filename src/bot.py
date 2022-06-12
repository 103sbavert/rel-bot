import os
import json
import nextcord
from nextcord.ext import commands

class RelBot(commands.Bot):

    def __init__(self, command_prefix=..., help_command=..., description=None, **options):
        super().__init__(command_prefix, help_command, description, **options)
        
    
    def is_ready(self) -> bool:
        super().is_ready()
        print("We're logged in!")
        
