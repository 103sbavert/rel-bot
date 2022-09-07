from discord import Object, Interaction
from discord.ui import View

from main.constants import fluency_levels
from main.views.view_components.buttons import FluencyLevelButton


class LevelsView(View):

    def __init__(self):
        super().__init__()
        for each in fluency_levels:
            self.add_item(FluencyLevelButton(each, self.on_fluencylevel_button_click))

    async def on_fluencylevel_button_click(self, button: FluencyLevelButton, interaction: Interaction):
        self.clear_items()
        interaction_user = interaction.user
        requested_role = interaction.guild.get_role(button.role_id)
        user_has_requested_role = interaction_user.get_role(requested_role.id)

        async def clear_roles():
            await interaction_user.remove_roles(
                Object(fluency_levels[0].role_id),
                Object(fluency_levels[1].role_id),
                Object(fluency_levels[2].role_id),
                Object(fluency_levels[3].role_id)
            )

        await clear_roles()
        if user_has_requested_role:
            await interaction.response.send_message(content="Role removed! You can now dismiss this message.", ephemeral=True)
        else:
            await interaction_user.add_roles(requested_role)
            await interaction.response.send_message(content="Role added! You can now dismiss this message.", ephemeral=True)
