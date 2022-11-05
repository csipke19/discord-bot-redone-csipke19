import commands.overwatch.hero as hero
import commands.overwatch.role as role

import utils


async def commands(msg, cmd=""):
    current_command = cmd[0]
    if len(cmd) > 1:
        cmd_parameter = cmd[1]

    ow_cmd_calls = {
        "role": [role.commands, "commands for role pick"],
        "hero": [hero.commands, "commands for hero pick"],

    }

    if len(cmd) == 1:
        await utils.list_command_details(msg.channel.send, ow_cmd_calls, current_command)
    elif cmd_parameter in ow_cmd_calls:
        await ow_cmd_calls[cmd_parameter][0](msg.channel.send, cmd)
    else:
        await utils.invalid_parameters(msg.channel.send, current_command)
