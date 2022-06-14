import json
import os
import bot

ENV_JSON_NAME = "env.json"
ENV_JSON_PATH = os.path.join(os.getcwd(), "", ENV_JSON_NAME)


def main():
    env_json_file = open(ENV_JSON_PATH) if os.path.exists(ENV_JSON_PATH) else None
    json_str = env_json_file.read()
    json_obj = json.loads(json_str)
    token = json_obj["bot_token"]
    rel_id = json_obj["rel-id"]
    print(rel_id)
    env_json_file.close()
    extension_list = ["cogs.prefix_commands_cog","cogs.slash_commands_cog"]
    rel_bot = bot.RelBot(extension_list, token, rel_id)
    rel_bot.run()


if __name__ == "__main__":
    main()
