import json
import discord


class RelBot(discord.Client):

    def __init__(self, token: str, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.token = token

    def run(self):
        super().run(self.token)



    
