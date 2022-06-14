import discord
from discord.ext import commands
#from discord import app_commands
#from discord.ui import Button
from .verification_role_view import VerificationRoleView

#class PrefixCommandsCog(commands.Cog, name="PrefixCommands"):
class VerificationButtonRolesCog(commands.Cog, name="Verification"):
   
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #This is necessary to ensure that it's persistent
        self.__bot.add_view(VerificationRoleView())
        print("Verification button view added")

    @commands.command()
    #@commands.is_owner()
    async def verification(self, ctx: commands.Context):
        await ctx.send("Have you read the rules? Tap/click the blue button.", view=VerificationRoleView())

# setup functions for bot
async def setup(bot):
    await bot.add_cog(VerificationButtonRolesCog(bot))
    #await bot.add_cog(PrefixCommandsCog(bot))