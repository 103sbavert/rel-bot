import os

from dotenv import load_dotenv

from keep_alive import keep_alive

from main.bot import RelBot
from main.constants import BOT_TOKEN_ENV_KEY, extension_list


def main():
    load_dotenv()
    # Retrieves bot token from the .env file so that the bot can log in
    token = os.getenv(BOT_TOKEN_ENV_KEY)
    rel_bot = RelBot(extension_list, str(token))
    keep_alive()
    rel_bot.run()


if __name__ == "__main__":
    main()
