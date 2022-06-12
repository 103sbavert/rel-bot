import bot
import json
import os

env_json = open(os.path.join("..", "env.json"))
TOKEN = json.load(env_json)

if __name__ == "__main__":
    bot.RelBot().
