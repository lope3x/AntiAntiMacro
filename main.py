from time import sleep
import pyautogui
import pydirectinput

from detect import detect

def repeatSkill(key, delay=0.5):
    sleep(delay)
    pydirectinput.press(key)

def re_enter_bg():
    if not check_if_should_enter_bg():
        return
    pydirectinput.keyDown('alt')
    pydirectinput.press('1')
    sleep(0.3)
    pydirectinput.keyUp('alt')

def check_if_should_enter_bg():
    eden = pyautogui.locateOnScreen('Helper_Images/eden_chat.png', confidence=0.7)
    return eden is not None

while True:
    re_enter_bg()
    sleep(0.1)
    detect()
    repeatSkill('f2', delay=5)
