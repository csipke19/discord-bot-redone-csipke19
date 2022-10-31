import pyautogui
from datetime import datetime


def create_screenshot(return_name=False):
    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    pic = pyautogui.screenshot()
    pic_name = 'screenshot'+now+".jpg"
    pic.save('screenshots/'+pic_name)
    if return_name:
        return pic_name
