import re


async def bot_moderation(message):
    member = message.author                     # Username with ID (Username#1234)
    username = str(member).split('#')[0]        # Username without ID (Username)
    user_message = re.split(r'\s+', str(message.content))

    if message.guild:
        for word in user_message:
            for key in moderated_words.keys():
                if word in moderated_words[key][1]:
                    await moderated_words[key][0](message)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')


async def clown(msg):
    emoji = "🤡"
    await msg.add_reaction(emoji)


moderated_words = {
    "cringe": [clown, ["cringe"]]
}