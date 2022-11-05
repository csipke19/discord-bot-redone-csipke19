import random

import utils


async def commands(send, cmd):
    if len(cmd) > 2:
        role_parameter = cmd[2]

    all_roles = ["damage", "support", "tank"]

    async def random_one_role():
        if len(cmd) < 4:
            await send("Your random role:\n" + random.choice(all_roles))
        else:
            await utils.invalid_parameters(send, " ".join(cmd[:2]))

    async def random_two_role():
        if len(cmd) < 4:
            roles = []
            while len(roles) != 2:
                role = random.choice(all_roles)
                if role not in roles:
                    roles.append(role)
            await send("Your random roles:\n" + ", ".join(roles))
        else:
            await utils.invalid_parameters(send, " ".join(cmd[:2]))

    role_calls = {
        "random": [random_one_role, "choose a random role to pick in overwatch"],
        "random_two": [random_two_role, "choose two random role to pick in overwatch"],
    }

    if len(cmd) == 2:
        await utils.list_command_details(send, role_calls, " ".join(cmd[:1]))
    elif role_parameter in role_calls:
        await role_calls[role_parameter][0]()
    else:
        await utils.invalid_parameters(send, " ".join(cmd[:1]))