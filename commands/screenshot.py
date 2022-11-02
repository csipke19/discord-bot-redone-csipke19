import utils
import discord


async def commands(msg, cmd=""):
    current_command = cmd[0]

    async def screenshot_take():
        utils.create_screenshot()
        await msg.channel.send("Screenshot taken and saved!")

    async def screenshot_send():
        picture_name = utils.create_screenshot(True)
        await msg.channel.send("Sending screenshot..")
        await msg.author.send(file=discord.File("screenshots/" + picture_name))
        await msg.channel.send("Screenshot sent successfully in DM!")

    screenshot_cmd_calls = {
        "take": [screenshot_take, "take and save the screenshot for the bot"],
        "send": [screenshot_send, "send the screenshot in DM for you"],

    }

    if len(cmd) == 1:
        await utils.list_command_details(msg.channel.send, screenshot_cmd_calls, current_command)
    elif cmd[1] in screenshot_cmd_calls:
        await screenshot_cmd_calls[cmd[1]][0]()
    else:
        await utils.invalid_parameters(msg.channel.send, current_command)
