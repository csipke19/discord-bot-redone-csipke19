import discord
import csv
import utils

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
    guild = client.get_guild(274905260718292992)
    voice_channels = guild.voice_channels
    for voice_channel in voice_channels:
        voice_channel_users[voice_channel.name] = voice_channel.members
        if voice_channel.members:
            for member in voice_channel.members:
                only_username = str(member)[:len(str(member)) - 5]
                users_in_channel[only_username] = voice_channel.name


@client.event
async def on_message(message):
    member = message.author                     # Username with ID (Username#1234)
    username = str(member).split('#')[0]        # Username without ID (Username)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if user_message.lower() == "szia bot":
        await message.channel.send("szia")
    if user_message.lower() == "screenshot":
        utils.create_screenshot()
        await message.channel.send("képernyőkép elkészítve")


def get_token():
    with open('csv_files/code.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0][0]


client.run(get_token())
