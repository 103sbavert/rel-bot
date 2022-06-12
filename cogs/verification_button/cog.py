from verification_role_view import VerificationRoleView
from nextcord.ext import commands

class VerificationButtonRolesCog(commands.Cog, name="Verification"):
    #Creates buttons that assign roles

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #Called when the bot is loaded, apparently
        self.__bot.add_view(VerificationRoleView())
        print("Verification button view added")

    @commands.command()
    #@commands.is_owner()
    async def verification(self, ctx: commands.Context):
        #Creates a new role view
        await ctx.send("Have you read the rules? Tap/click the blue button.", view=VerificationRoleView())

# setup functions for bot
def setup(bot):
    bot.add_cog(VerificationButtonRolesCog(bot))