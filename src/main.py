import bot
import json
import os

ENV_JSON_NAME = "env.json"
ENV_JSON_PATH = os.path.join(os.getcwd, "..", ENV_JSON_NAME)


def main():
    env_json_file = open(ENV_JSON_PATH) if os.path.exists(ENV_JSON_PATH) else None
    json_str = env_json_file.read()
    json_obj = json.loads(json_str)
    token = json_obj["bot_token"]
    rel_bot = bot.RelBot(token)
    rel_bot.run()
    env_json_file.close()


if __name__ == "__main__":
    main()
