import os
from dotenv.main import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

TESTING_GUILD_ID = 580707576942034955

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run(os.getenv("BOT_TOKEN"))
