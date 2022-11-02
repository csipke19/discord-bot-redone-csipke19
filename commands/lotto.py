import utils
import random


async def commands(msg, cmd=""):
    current_command = cmd[0]
    if len(cmd) > 1:
        parameter = cmd[1]

    async def lotto_send(num):
        if num is None:
            return
        numbers = await generate_numbers(num)
        await msg.channel.send("The lotto numbers are the following:\n"+", ".join(numbers))

    async def generate_numbers(max_number):
        numbers = []
        while len(numbers) != max_number:
            number = str(random.randint(1, 91))
            if number not in numbers:
                numbers.append(number)
        return numbers

    lotto_cmd_calls = {
        "five": [lotto_send, "Generate five random numbers for lotto"],
        "six": [lotto_send, "Generate six random numbers for lotto"],
        "seven": [lotto_send, "Generate seven random numbers for lotto"],

    }

    def convert_to_number(number):
        parameter_numbers = {"five": 5, "six": 6, "seven": 7, }
        if number in parameter_numbers:
            return parameter_numbers[number]
        else:
            return None

    if len(cmd) == 1:
        await utils.list_command_details(msg.channel.send, lotto_cmd_calls, current_command)
    elif parameter in lotto_cmd_calls:
        await lotto_cmd_calls[parameter][0](convert_to_number(parameter))
    else:
        await utils.invalid_parameters(msg.channel.send, current_command)
