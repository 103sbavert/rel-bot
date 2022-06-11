import os
from dotenv.main import load_dotenv
from nextcord import Intents

load_dotenv()

PREFIX = "€"
BOT_NAME = "r/EnglishLearning"
BOT_TOKEN = os.getenv('THE_BOT_TOKEN')

#Role IDs

UNVERIFIED_ROLE_ID = int(os.getenv("UNVERIFIED_ROLE_TOKEN", ""))

NATIVE_SPEAKER_ROLE_ID = int(os.getenv("NATIVE_SPEAKER_ROLE_TOKEN", ""))
ADVANCED_ROLE_ID = int(os.getenv("ADVANCED_ROLE_TOKEN", ""))
INTERMEDIATE_ROLE_ID = int(os.getenv("INTERMEDIATE_ROLE_TOKEN", ""))
BEGINNER_ROLE_ID = int(os.getenv("BEGINNER_ROLE_TOKEN", ""))

#Intents

BOT_INTENTS = (
    Intents(messages=True, message_content=True, guilds=True)
)