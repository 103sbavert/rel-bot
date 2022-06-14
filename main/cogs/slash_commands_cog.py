import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Select

from main.views.roles_view import RolesView


class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    class MySelect(Select):
        async def callback(self, interaction):
            await interaction.response.send_message(f"You chose: {self.values[0]}")

    @app_commands.command(name="roles")
    async def roles(self, interaction: discord.Interaction):
        view = RolesView()
        await interaction.response.send_message("Choose a catergory to select a role from", view=view, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
