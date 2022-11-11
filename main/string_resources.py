from main.constants import channels


class StringResources:
    slash_command_cog_name = "SlashCommand"
    helper_message_cog_name = "HelperMessage"
    fluency_roles_cog_name = "FluencyRoles"
    roles_command_name = "roles"
    roles_command_description = "Select a role from the categories available!"
    bot_description = ""
    roles_command_message = ""
    helper_message_cog_string: str = f"Please, go to <#{channels['english_level']}> and select a role that fits your fluency level to access the rest of the server"
    FLUENCY_MESSAGE_ID_KEY = "fluency_message_id"
    LANGUAGES_MESSAGE_ID_KEY = "languages_message_id"
    MISC_MESSAGE_ID_KEY = "misc_message_id"
