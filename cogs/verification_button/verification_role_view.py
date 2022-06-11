import nextcord
import config

VIEW_NAME = "VerificationRoleView"

#Follow the video to eventually move this to another file because it will be neater
def custom_id(view: str, id: int) -> str:
    #Return the view with the ID
    return f"{config.BOT_NAME}:{view}:{id}"

class VerificationRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        #if user has the role already
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                f"Your {role.name} role has been removed.",
                ephemeral=True
            )
        #if user doesn't yet have the role
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                f"You've been given the {role.name} role.",
                ephemeral=True
            )

    @nextcord.ui.button(
        label="Yes, and I am not a bot!",
        #emoji = "📖",
        style=nextcord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.UNVERIFIED_ROLE_ID),
    )
    async def verification_button(self, button, interaction):
        #await interaction.response.send_message("Clicked Verification button")
        await self.handle_click(button, interaction)

    