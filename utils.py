import pyautogui
from datetime import datetime


def create_screenshot(return_name=False):
    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    pic = pyautogui.screenshot()
    pic_name = 'screenshot'+now+".jpg"
    pic.save('screenshots/'+pic_name)
    if return_name:
        return pic_name


async def list_command_details(msg, parameters, command):
    await msg(f"The command have the following parameters: \n (Usage: {command} (parameter) )")
    await msg("\n".join("{} - {}".format(k, v[1]) for k, v in parameters.items()))


async def invalid_parameters(msg,command):
    await msg(f"Invalid parameters, write in '{command}' for more details!")
