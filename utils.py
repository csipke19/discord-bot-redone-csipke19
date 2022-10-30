import pyautogui
from datetime import datetime


def create_screenshot():
    now = datetime.now()
    pic = pyautogui.screenshot()
    pic.save('screenshots/screenshot'+now)