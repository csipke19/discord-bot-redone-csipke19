import utils
import random


async def commands(send, cmd):
    if len(cmd) > 2:
        hero_parameter = cmd[2]
    all_hero_name = {
        "dmg": ["Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei",
                "Pharah", "Soldier:76", "Sojourn", "Sombra", "Symmetra", "Torbjörn", "Tracer", "Widowmaker"],
        "supp": ["Ana", "Baptiste", "Brigitte", "Kiriko", "Lúcio", "Mercy", "Moira", "Zenyatta"],
        "tank": ["D.Va", "Doomfist", "Junker Queen", "Orisa", "Reinhardt", "Roadhog", "Sigma", "Winston",
                 "Wrecking Ball"],
    }

    async def random_hero():
        if len(cmd) > 3:
            role = cmd[3]
        if len(cmd) == 3:
            await send("!ow hero random <role>\nChoose a role with: dmg, supp, tank")
        elif role in all_hero_name:
            await send("Your random hero is:\n" + random.choice(all_hero_name[role]))
        else:
            await utils.invalid_parameters(send, " ".join(cmd[:2]))

    async def choose_hero():
        if len(cmd) == 3:
            await send("!ow hero choose <hero1> <hero2> <hero3>...\nChoose a hero from the given names")
        else:
            await send("Your random hero is:\n" + random.choice(cmd[4:]))

    hero_calls = {
        "random": [random_hero, "choose a random hero from the given role. (roles: damage, support, tank)"],
        "choose": [choose_hero, "choose a random hero from the given names. (put spaces between the names)"],
    }

    if len(cmd) == 2:
        await utils.list_command_details(send, hero_calls, " ".join(cmd[:1]))
    elif hero_parameter in hero_calls:
        await hero_calls[hero_parameter][0]()
    else:
        await utils.invalid_parameters(send, " ".join(cmd[:1]))