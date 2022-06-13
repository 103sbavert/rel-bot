import discord
from discord.ext import commands
from discord import app_commands


class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roles")
    async def roles(self, interaction: discord.Interaction):
        await interaction.response.send_message("something", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
