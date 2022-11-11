import os
from os import getcwd

import discord
from discord.ext import commands

from main.constants import channels, rel_id
from main.string_resources import StringResources
from main.views.levels_view.levels_view import LevelsView


class FluencyRoles(commands.Cog, name="FluencyRoles"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def post_fluency_roles_view(self):
        rel = discord.utils.get(self.bot.guilds, id=rel_id)
        levels_channel = discord.utils.get(rel.channels, id=channels["english_level"])
        fluency_message_id = os.getenv(StringResources.FLUENCY_MESSAGE_ID_KEY)
        if fluency_message_id is None:
            fluency_message = await levels_channel.send(content="Choose a fluency level...", view=LevelsView())
            dotenv_path = f"{getcwd()}/../.env"
            with open(dotenv_path, mode="a+") as dotenv:
                dotenv.write(f"{StringResources.FLUENCY_MESSAGE_ID_KEY}={str(fluency_message.id)}")
        else:
            await levels_channel.get_partial_message(int(os.getenv(StringResources.FLUENCY_MESSAGE_ID_KEY))).edit(view=LevelsView())
            print(os.getenv(StringResources.FLUENCY_MESSAGE_ID_KEY))


async def setup(bot: commands.Bot):
    await bot.add_cog(FluencyRoles(bot))
