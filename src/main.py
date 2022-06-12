import bot
import json
import os

ENV_JSON_PATH = os.path.join('..', "env.json")

if os.path.exists(ENV_JSON_PATH):
    global env_json
    env_json = open(os.path.join("..", "env.json"), encoding="utf-8")

json_str = env_json.read()
json_obj = json.loads(json_str)

bot.RelBot().run(json_obj["bot_token"])
