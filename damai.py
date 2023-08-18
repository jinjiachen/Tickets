#coding=utf-8

import pyautogui
import time
from pymouse import PyMouse

m=PyMouse()
duration=input('输入运行时长')
now=time.time()
while time.time()-now<=int(duration):
#    pyautogui.click(1150,935,duration=0.0001)
    m.click(1150,935,1)
#    pyautogui.click(1041,935)
