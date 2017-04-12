#!/usr/bin/env python3

import pyautogui
import time


while True:
    pos = pyautogui.position()
    print(pos)
    time.sleep(0.1)
    if pos[0] > 500 or pos[1] > 500:
        pyautogui.moveTo(35, 35, duration=0.5)
        time.sleep(0.1)
        pyautogui.click()
        pyautogui.typewrite('gedit')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.moveTo(1725, 1050)
        pyautogui.typewrite('Karny kutas za niezablokowanie ekranu!!!')
        exit(0)


