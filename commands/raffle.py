import random
import time

import utils

current_command = ""
reaction_emoji = '✅'
participants = []
is_open = False
owner = None
item = ""
is_sent = True


async def commands(msg, cmd=""):
    global current_command
    current_command = cmd[0]
    send = msg.channel.send
    if len(cmd) > 1:
        parameter = cmd[1]
    if len(cmd) > 3:
        await send(f"Invalid command parameter number, please use {current_command} for more details!")
        return

    async def raffle_open():
        global is_sent, item, participants, is_open, owner
        await msg.delete()
        if is_sent and not is_open:
            is_sent = False
            is_open = True
            item = cmd[2]
            participants = []
            owner = msg.author
            await send(f"A raffle is opened by: {owner.name}! Join the raffle with: '!raffle join' !")
        else:
            await send("A raffle is currently going on, please shut down the current one first!")

    async def raffle_close():
        global is_open
        if owner is None:
            await send("There is no active raffle currently!")
            return
        if not is_sent:
            if is_open:
                is_open = False
                await send("The raffle has been closed!")
            else:
                await send("The raffle is currently closed!")

    async def raffle_join():
        for member in participants:
            if msg.author.name == member.name:
                await send(f"You already joined this raffle {str(msg.author).split('#')[0]}!")
                await msg.delete()
                return
        participants.append(msg.author)
        await msg.add_reaction(reaction_emoji)

    async def raffle_start():
        if owner is None:
            await send("There is no active raffle currently!")
            return
        if msg.author.name == owner.name:
            if not is_open:
                winner = random.choice(participants)
                await send("and the winner is...")
                time.sleep(3)
                await send(f".. {winner.name}! Your item is sent through DM, congratulations!")
                await winner.send(f"You have won the following item:\n{item}")
                await raffle_terminate()
            else:
                await msg.author.send("The raffle is currently open, please close it first!")

    async def raffle_status():
        if owner is None:
            await send("There is no active raffle currently!")
            return
        if is_open:
            await send("The raffle is currently open! You can join with '!raffle join'! ")
        else:
            await send("The raffle is currently closed! You can't join to the raffle right now!")

    async def raffle_owner():
        if owner is None:
            await send("There is no owner for the raffle or no raffle at all!")
        else:
            await send(f"The current raffle owner is: {owner.name}")

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