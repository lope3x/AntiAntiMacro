from time import sleep
import pyautogui
import pydirectinput
import os

def get_folder_files(path):
    files = os.listdir(path)

    return files

def take_temp_screenshot():
    temps = get_folder_files('NonSavedPrints')
    lastTemp = int(temps[-1].split('.')[0][-1])

    nextTemp = lastTemp + 1

    pyautogui.screenshot(f'NonSavedPrints/temp{nextTemp}.png')

def insert_password(password):
    pydirectinput.write(password, interval=0.25)
    pydirectinput.press('enter')

def detect():
    start = pyautogui.locateOnScreen('trava.png', confidence=0.7)

    if start is not None:
        print('start')
        files = get_folder_files('Images')

        flag = False


        for file in files:
            locatedSpot = pyautogui.locateOnScreen(f'Images/{file}', confidence=0.7)

            if locatedSpot is not None:
                print(file)
                password = file.split('.')[0]
                insert_password(password)
                pydirectinput.press('enter')
                flag = True

        if flag is False:
            take_temp_screenshot()

def repeatSkill(key, delay=0.5):
    sleep(delay)
    pydirectinput.press(key)

def re_enter_bg():
    pydirectinput.keyDown('alt')
    pydirectinput.press('1')
    sleep(0.3)
    pydirectinput.keyUp('alt')

while True:
    re_enter_bg()
    sleep(0.1)
    detect()
    repeatSkill('f2', delay=5)
