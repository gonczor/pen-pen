#!/usr/bin/env python3

import subprocess
import platform
import pyautogui
import time


system = platform.system()

website = "http://www.google.com/images"
search = 'karny kurtas'
editor = ''
command = []

if system == 'Linux':
    editor = 'gedit'
    command = ['xdg-open', website]
elif system == 'Windows':
    editor = 'Notepad'
    # TODO to be implemented

pyautogui.moveTo(35, 35, duration=0.5)
while True:
    pos = pyautogui.position()
    print(pos)
    time.sleep(0.1)
    if pos[0] > 500 or pos[1] > 500:
        pyautogui.moveTo(35, 35, duration=0.5)
        time.sleep(0.1)
        pyautogui.press('winleft')
        pyautogui.typewrite(editor)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.typewrite('Karny kutas za niezablokowanie ekranu!!!')
        subprocess.call(command)
        time.sleep(5)
        pyautogui.typewrite('Karny kutas')
        pyautogui.press('enter')
        exit(0)

