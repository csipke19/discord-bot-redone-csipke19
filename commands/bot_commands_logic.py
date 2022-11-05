import re

import commands.screenshot as screenshot
import commands.lotto as lotto
import commands.raffle as raffle
import commands.overwatch.ow as overwatch


async def bot_commands(message):
    member = message.author                     # Username with ID (Username#1234)
    username = str(member).split('#')[0]        # Username without ID (Username)
    user_message = str(message.content)
    command_call = user_message.split(maxsplit=1)[0]
    if message.guild:
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')
    if command_call in command_calls:
        print(f'{username}: {user_message}')
        if command_call == "!help":
            await command_calls[command_call][0](message)
        else:
            await command_calls[command_call][0](message, user_message.split(" "))


async def help_command(msg):
    await msg.channel.send("The bot have the following commands: ")
    await msg.channel.send("\n".join("{} - {}".format(k, v[1]) for k, v in command_calls.items()))


command_calls = {
    "!help": [help_command, "list out all the bot commands"],
    "!screenshot": [screenshot.commands, "take screenshot from the monitor of the bot running server"],
    "!lotto": [lotto.commands, "generate lotto numbers"],
    "!raffle": [raffle.commands, "manage a raffle (start, join, stop.. etc.)"]
}