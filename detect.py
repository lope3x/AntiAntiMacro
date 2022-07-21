import os
from time import sleep

import pyautogui
import pydirectinput


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
    start = pyautogui.locateOnScreen('Helper_Images/trava.png', confidence=0.7)

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


if __name__ == '__main__':
    detect()
    sleep(1)
