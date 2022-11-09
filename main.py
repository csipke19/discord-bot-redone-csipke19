import discord
import csv
from commands import bot_commands_logic as commands
from moderations import bot_moderations_logic as moderations

intents = discord.Intents.default()
#intents = discord.Intents.all()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
guild = 0
app_info = None
bot_owner_user = None
bot_owner_name = ""
users_in_channel = dict()       # Key: String - Value: String
voice_channel_users = dict()    # Key: String - Value: MemberClass
is_automoderate = True
server_id = None


@client.event
async def on_ready():
    global users_in_channel
    global app_info
    global bot_owner_user
    global bot_owner_name
    print("We have logged in as {0.user}".format(client))
    app_info = await client.application_info()
    bot_owner_user = app_info.owner
    bot_owner_name = bot_owner_user.name
    fill_voice_channel_users()
    print("Voice channel users successfully added to the lists!") if len(users_in_channel) > 0 and len(voice_channel_users) > 0 else print("There are no voice channel users or we had a problem")


def fill_voice_channel_users():
    global guild
    guild = client.get_guild(server_id)
    voice_channels = guild.voice_channels
    for voice_channel in voice_channels:
        voice_channel_users[voice_channel.name] = voice_channel.members
        if voice_channel.members:
            for member in voice_channel.members:
                only_username = str(member)[:len(str(member)) - 5]
                users_in_channel[only_username] = voice_channel.name


@client.event
async def on_voice_state_update(member, before, after):
    global users_in_channel
    global voice_channel_users
    only_username = str(member)[:len(str(member)) - 5]
    try:
        users_in_channel[only_username] = after.channel.name
    except:
        users_in_channel.pop(only_username)
    try:
        if voice_channel_users[before.channel.name]:
            voice_channel_users[before.channel.name].remove(member)
    except:
        pass
    if after.channel:
        voice_channel_users[after.channel.name].append(member)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif str(message.content.strip())[0] != "!" and is_automoderate:
        await moderations.bot_moderation(message)
    else:
        await commands.bot_commands(message)


def get_token():
    with open('csv_files/code.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0][0]


def set_server_id(id_value):
    global server_id
    server_id = int(id_value)


def set_automoderate(boolean_value):
    global is_automoderate
    is_automoderate = True if boolean_value == "True" else False


config_file_parameters = {
    "server_id": set_server_id,
    "automoderate": set_automoderate
}


def load_cfg():
    with open('settings.cfg', newline='') as f:
        for parameter in f:
            line = parameter.strip().split("=")
            key = line[0].strip()
            value = line[1].strip()
            if key in config_file_parameters:
                config_file_parameters[key](value)


load_cfg()
client.run(get_token())
