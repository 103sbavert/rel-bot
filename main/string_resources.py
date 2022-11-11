from main.constants import channels


class StringResources:
    slash_command_cog_name = "SlashCommands"
    helper_messages_cog_name = "HelperMessages"
    fluency_roles_cog_name = "FluencyRoles"
    roles_command_name = "roles"
    prune_command_name = "prune"
    
    roles_command_description = "Select a role from the categories available!"
    prune_command_description = "Prune users who do not have a role"
    
    bot_description = ""
    roles_command_message = ""
    
    helpChannel_message: str = f"Hi! To finish joining the server, you should go to the channel called <#{channels['english_level']}> and follow the instructions there!"
    talkerPing_message = "Great, now join a voice channel and wait!"
    
    FLUENCY_MESSAGE_ID_KEY = "fluency_message_id"
    LANGUAGES_MESSAGE_ID_KEY = "languages_message_id"
    MISC_MESSAGE_ID_KEY = "misc_message_id"
