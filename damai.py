#coding=utf-8

import pyautogui
from pymouse import PyMouse

m=PyMouse()
for i in range(1,50):
    print(i)
#    pyautogui.click(1150,935,duration=0.0001)
    m.click(1150,935,1)
#    pyautogui.click(1041,935)
