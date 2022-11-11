import discord
from discord import app_commands
from discord.ext import commands
from main.constants import fluency_levels, bot_role
from main.views.roles_view.roles_view import RolesView
from main.string_resources import StringResources

class SlashCommandsCog(commands.Cog, name="SlashCommands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    # Roles command that brings up the menu for choosing a role
    @app_commands.command(name=StringResources.roles_command_name, description=StringResources.roles_command_description)
    async def roles(self, interaction: discord.Interaction):
        view = RolesView()
        await interaction.response.send_message(StringResources.roles_command_message, view=view, ephemeral=True)

    # Prune command that kicks members with no fluency role or bot role   
    @app_commands.command(name=StringResources.prune_command_name, description=StringResources.prune_command_description)
    @commands.has_role("Server Bot Team")
    async def prune(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        members = interaction.guild.members
        roles = [interaction.guild.get_role(fluency_levels[0].role_id), interaction.guild.get_role(fluency_levels[1].role_id), 
                 interaction.guild.get_role(fluency_levels[2].role_id), interaction.guild.get_role(fluency_levels[3].role_id),
                 interaction.guild.get_role(bot_role)]
        count = 0 
        # If member doesn't have a role in the list roles then they will be kicked
        for member in members:
            check = any(item in roles for item in member.roles)
            if not check:
                await interaction.guild.kick(member)    
                count = count + 1   
                # Max 50 members to be kicked at once to avoid being timed out by Discord for sending too many requests
                if count >= 50:
                    break    
        await interaction.followup.send('Kicked ' + str(count) + ' member(s)')


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommandsCog(bot))
