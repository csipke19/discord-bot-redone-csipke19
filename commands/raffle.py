import random
import time

import utils
import discord
from discord.utils import get

current_command = ""
reaction_emoji = '✅'
participant_ids = []
is_open = False
owner = None
item = ""
is_sent = True


async def commands(msg, cmd=""):
    global current_command
    current_command = cmd[0]
    if len(cmd) > 1:
        parameter = cmd[1]
    if len(cmd) > 3:
        await msg.channel.send(f"Invalid command parameter number, please use {current_command} for more details!")
        return

    async def raffle_open():
        global is_sent, item, participant_ids, is_open, owner
        if is_sent and not is_open:
            is_sent = False
            is_open = True
            item = cmd[2]
            participant_ids = []
            owner = str(msg.author).split('#')[0]
            await msg.channel.send(f"A raffle is opened by: {owner}! Join the raffle with: '!raffle join' !")
        else:
            await msg.channel.send("A raffle is currently going on, please shut down the current one first!")

    async def raffle_close():
        pass

    async def raffle_join():
        if msg.author not in participant_ids:
            participant_ids.append(msg.author)
            await msg.add_reaction(reaction_emoji)
        else:
            await msg.reply(f"You already joined this raffle {str(msg.author).split('#')[0]}!")

    async def raffle_start():
        await msg.channel.send("and the winner is...")
        time.sleep(4)
        await msg.channel.send(f".. {random.choice(participant_ids)}! Your item is sent through DM, congratulations!")
        get(discord.Member,)

    async def raffle_status():
        pass

    async def raffle_owner():
        pass

    async def raffle_participants():
        pass

    async def raffle_send_item():
        pass

    async def raffle_terminate():
        pass

    screenshot_cmd_calls = {
        "open": [raffle_open, "open a raffle with the give item (e.g.: cd-key) (Usage: !raffle open <item_for_raffle>)"],
        "close": [raffle_close, "close the ongoing raffle from new joiners"],
        "join": [raffle_join, "join to the ongoing raffle"],
        "start": [raffle_start, "start the raffle with the joined participants. You need to close the raffle first"],
        "participants": [raffle_participants, "list out the current participants to the raffle"],
        "status": [raffle_status, "show the current status of the ongoing raffle (open/closed)"],
        "owner": [raffle_owner, "show the owner of the ongoing raffle"],
        "item": [raffle_send_item, "send the currently raffled item in DM (need to be owner for this)"],
        "terminate": [raffle_terminate, "terminate the current raffle without item raffle"]

    }

    if len(cmd) == 1:
        await utils.list_command_details(msg.channel.send, screenshot_cmd_calls, current_command)
    elif cmd[1] in screenshot_cmd_calls:
        await screenshot_cmd_calls[cmd[1]][0]()
    else:
        await utils.invalid_parameters(msg.channel.send, current_command)