import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View


class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    class MySelect(Select):
        async def callback(self, interaction):
            await interaction.response.send_message(f"You chose: {self.values[0]}")
            
    @app_commands.command(name="roles")
    async def roles(self, interaction: discord.Interaction):
        select = SlashCommandsCog.MySelect(
            placeholder = "Choose a catergory",
            options=[
                discord.SelectOption(label="English Level", emoji ="📖", description ="Roles that best represents your English level"),
                discord.SelectOption(label="Languages", emoji ="📚", description ="Roles to display what languages you speak"),
                discord.SelectOption(label="Other", emoji ="📃", description ="Other roles"),
            ])
        

        
        view = View()
        view.add_item(select)
        await interaction.response.send_message("Choose a catergory to select a role from", view=view, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
