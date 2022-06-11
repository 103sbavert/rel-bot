import os
from dotenv.main import load_dotenv
import nextcord
from nextcord.ext import commands
from config import BOT_INTENTS

load_dotenv()

TESTING_GUILD_ID = 580707576942034955

#bot = commands.Bot() #command_prefix=config.PREFIX doesn't work
client = commands.Bot(command_prefix="=", intents=BOT_INTENTS)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # load all cogs
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        client.load_extension(f"cogs.{folder}.cog")

@client.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

client.run(os.getenv("BOT_TOKEN"))
