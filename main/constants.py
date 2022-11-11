class RoleCategory:
    def __init__(self, label, code):
        self.label = label
        self.code = code

# Defines role class for storing role IDs
class Role:

    def __init__(self, role_id, label):
        self.role_id = role_id
        self.label = label


BOT_TOKEN_ENV_KEY = "bot_token"

extension_list = [
    "main.cogs.slash_commands_cog",
    "main.cogs.helper_messages_cog",
    "main.cogs.fluency_roles_cog"
]

# Defines role catergories
roles_categories = [
    RoleCategory("Fluency", "1"),
    RoleCategory("Native Language", "2"),
    RoleCategory("Misc", "3"),
    RoleCategory("Pronoun", "4")
]


bot_role = 580829130581475339
rel_id = 580707576942034955
talker_role = 654600359767048212 

channels = {
    "roles": 874727627989078016,
    "help": 874753509118066729,
    "english_level": 874727627989078016
}


fluency_levels = [
    Role(580751306495623168, "Beginner"),
    Role(580751510246260757, "Intermediate"),
    Role(580751767541907496, "Advanced"),
    Role(580751998752784385, "Native Speaker")
]

supported_languages = [
    Role(886506885497376848, "Zulu"),
    Role(813905117974888459, "Welsh"),
    Role(640081114240778250, "Walloon"),
    Role(654616034044674058, "Ukrainian"),
    Role(654397063726891038, "Tulu"),
    Role(650907935400263690, "Vietnamese"),
    Role(587522512913432599, "Turkish"),
    Role(715266409927540737, "Thai"),
    Role(623396464793747492, "Telugu"),
    Role(641497102312013825, "Tamil"),
    Role(650196773926731776, "Taiwanese"),
    Role(684513861818384484, "Swedish"),
    Role(925445760252772462, "Swahili"),
    Role(928338020728471583, "Somali"),
    Role(783090904327389226, "Slovene"),
    Role(687044307156467753, "Slovak"),
    Role(787630989094289418, "Sinhala"),
    Role(588599137696612352, "Spanish"),
    Role(677025992514207757, "Serbian"),
    Role(654678862428373012, "Sindhi"),
    Role(647798355866681348, "Romanian"),
    Role(654629480903606284, "Punjabi"),
    Role(587748703071371264, "Russian"),
    Role(642829973975072781, "Polish"),
    Role(587394109807919119, "Portuguese (PT/BR)"),
    Role(687002123862540345, "Persian"),
    Role(614063956046381066, "Pashto"),
    Role(679544033475166219, "Norwegian"),
    Role(758686954744578079, "Nepali"),
    Role(665481298202066954, "Mongolian"),
    Role(638631211576852487, "Marathi"),
    Role(587713217522827274, "Mandarin"),
    Role(768891599953854526, "Malayalam"),
    Role(729656496589373442, "Malay"),
    Role(740645005546487879, "Lithuanian"),
    Role(607927236309286954, "Latvian"),
    Role(613999459616948235, "Kyrgyz"),
    Role(715107339623071784, "Kurdish"),
    Role(612656913124950018, "Korean"),
    Role(645834622545952798, "Kazakh"),
    Role(654396813549371422, "Kannada"),
    Role(588473951160893460, "Japanese"),
    Role(625415802706853894, "Indonesian"),
    Role(587389573206638602, "Italian"),
    Role(649322239761711125, "Hungarian"),
    Role(588838823358889995, "Hindustani"),
    Role(673488869504712715, "Hebrew"),
    Role(643432051319767050, "Gujarati"),
    Role(640644915704889414, "Greek"),
    Role(588390707744604169, "German"),
    Role(688102252816105556, "Georgian"),
    Role(645932033616379915, "Garhwali"),
    Role(594887234746974209, "French"),
    Role(652557007114600488, "Finnish"),
    Role(642680325834801164, "Filipino"),
    Role(639583461086330880, "Farsi"),
    Role(648643045058936832, "Estonian"),
    Role(607670212707483649, "Dutch"),
    Role(647170785521303562, "Danish"),
    Role(633177096830713857, "Czech"),
    Role(661528595272958013, "Cantonese"),
    Role(663679343310143520, "Burmese"),
    Role(642841725341270066, "Bulgarian"),
    Role(652427910887505930, "Bengali"),
    Role(628257738971152385, "Belarusian"),
    Role(660089597727997982, "Baniya"),
    Role(785896912800841739, "Azerbaijani"),
    Role(834011545922174996, "Armenian"),
    Role(736873280648118292, "Amharic"),
    Role(612690301257252874, "Arabic"),
    Role(612173454388625408, "Afrikaans"),
]

misc_roles = [
    Role(581981082262700043, "Helper"),
    Role(776459201366589490, "Beginner Friendly"),
    Role(654600359767048212, "Talker"),
    Role(753485493324480592, "Conversationalist"),
    Role(680828119157833841, "Correct Me"),
    Role(755146054067945573, "Server Music"),
    Role(742386672523542560, "Brain of the Week"),
    Role(692048978384257136, "Server Games"),
    Role(865633878970597377, "Psychology Event"),
]

pronoun_roles = [
    Role(753484926682267688, "He/Him"),
    Role(753485324013011016, "She/Her"),
    Role(753505984835616848, "They/Them")
]
