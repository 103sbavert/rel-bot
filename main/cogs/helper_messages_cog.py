from __future__  import annotations
from main.string_resources import StringResources
from main.constants import channels, talker_role
from os import getcwd
import discord
from discord.ext import commands

class HelperMessagesCog(commands.Cog, name="HelperMessages"):
    class IDAlreadyExistsError(Exception):

        def __init__(self, user_id: int | str) -> None:
            self.user_id = user_id

        def __str__(self):
            return f"User {self.user_id} has already been helped"

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @staticmethod
    def add_user(user_id: int):
        with open(f"{getcwd()}/../helped_users", encoding="utf-8", mode="a+") as file:
            ids = file.readline()
            if ids.find(str(user_id)) != -1:
                raise HelperMessagesCog.IDAlreadyExistsError(user_id)
            file.write(f"{user_id}\n")

    @staticmethod
    def user_exists(user_id: int) -> bool:
        with open(f"{getcwd()}/../helped_users", encoding="utf-8", mode="a+") as file:
            ids = file.readline()
            return True if ids.find(str(user_id)) != -1 else False

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        requires_help = message.channel.id == channels["help"] and \
                        not message.author.bot and \
                        len(message.author.roles) == 1
                        #broken
                        #HelperMessagesCog.user_exists(message.author.id)

        if requires_help:
            await message.reply(StringResources.helpChannel_message)
            HelperMessagesCog.add_user(message.author.id)
        # Checks to see if the Talker role has been mentioned
        # Automatically responds to them if so
        mentions = message.raw_role_mentions 
        for mention in mentions:
            if mention == talker_role:
                await message.reply(StringResources.talkerPing_message)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelperMessagesCog(bot))
