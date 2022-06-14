import discord
import os
import json

#Yes, this is messy. Chastise me later lol
ENV_JSON_NAME = "env.json"
ENV_JSON_PATH = os.path.join(os.getcwd(), "", ENV_JSON_NAME)
env_json_file = open(ENV_JSON_PATH) if os.path.exists(ENV_JSON_PATH) else None
json_str = env_json_file.read()
json_obj = json.loads(json_str)
unverified_id = json_obj["role_ids"][0]["unverified"]
rel_id = json_obj["rel-id"]
bot_name = "r/EnglishLearning"
print(rel_id)
view_name = "VerificationRoleView"

#Eventually move this to another file because it will be neater
def custom_id(view: str, id: int) -> str:
    #Return the view with the ID
    return f"{bot_name}:{view}:{id}"

class VerificationRoleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: discord.ui.Button, interaction: discord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        #role_id = "unverified_id" #would need to add a guild ID to the Button, but I don't know how to do that
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, discord.Role)
        #if user has the role already
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
        #if user doesn't yet have the role
        else:
            await interaction.user.add_roles(role)

    @discord.ui.button(
        label="Yes, and I am not a bot!",
        #emoji = "📖",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(view_name, unverified_id),
    )
    async def verification_button(self, button, interaction):
        await self.handle_click(button, interaction)

    