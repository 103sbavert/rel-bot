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
            fluency_chooser = discord.Embed(title="What is your fluency level in English?",
                                            url="https://discord.com/channels/580707576942034955/874727627989078016/875772511659372574",
                                            color=0x00FFFF)
            fluency_chooser.add_field(name="Beginner", value="You only speak a little English\n(CEFR A1/A2)", inline=False)
            fluency_chooser.add_field(name="Intermediate (Select this if you are unsure)", value="You can usually express yourself\n(CEFR B1/B2)",
                                      inline=False)
            fluency_chooser.add_field(name="Advanced", value="Fluent or nearly fluent, but not native\n(CEFR C1/C2)", inline=False)
            fluency_chooser.add_field(name="Native Speaker", value="English was your primary language when growing up at home or at school",
                                      inline=False)

            fluency_message = await levels_channel.send(embed=fluency_chooser, view=LevelsView())
            dotenv_path = f"{getcwd()}/.env"
            with open(dotenv_path, mode="a+") as dotenv:
                dotenv.write(f"{StringResources.FLUENCY_MESSAGE_ID_KEY}={str(fluency_message.id)}")
        else:
            await levels_channel.get_partial_message(int(os.getenv(StringResources.FLUENCY_MESSAGE_ID_KEY))).edit(view=LevelsView())
            print(os.getenv(StringResources.FLUENCY_MESSAGE_ID_KEY))


async def setup(bot: commands.Bot):
    await bot.add_cog(FluencyRoles(bot))
