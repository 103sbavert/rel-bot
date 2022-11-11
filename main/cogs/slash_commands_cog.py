import discord
from discord import app_commands
from discord.ext import commands

from main.string_resources import StringResources
from main.views.roles_view.roles_view import RolesView


class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name=StringResources.roles_command_name, description=StringResources.roles_command_description)
    async def roles(self, interaction: discord.Interaction):
        view = RolesView()
        await interaction.response.send_message(StringResources.roles_command_message, view=view, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
