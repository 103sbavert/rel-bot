import discord
from discord import app_commands
from discord.ext import commands

from main.views.roles_view import RolesView


class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roles", description="Select a role from the categories available!")
    async def roles(self, interaction: discord.Interaction):
        view = RolesView()
        await interaction.response.send_message("Choose a catergory to select a role from", view=view, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
