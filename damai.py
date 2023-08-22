#coding=utf-8

import pyautogui
import time
import os
from pymouse import PyMouse

m=PyMouse()
start=input('开始抢票的时间：')
data=start.split(':')
duration=input('输入运行时长')
while True:
    data_live=time.strftime('%H:%M:%S').split(':')
    data_min=int(data[1])-int(data_live[1])
    data_sec=abs(int(data[2])-int(data_live[2]))
    print('当前时间：',time.strftime('%H:%M:%S'))
    print('设定时间：',start)
    print('倒计时：%s分%s秒'%(data_min-1,60-data_sec))
    os.system('cls')
    if time.strftime("%H:%M:%S")==start:
        now=time.time()
        while time.time()-now<=int(duration):
            m.click(1150,935,1)
#          pyautogui.click(1150,935,duration=0.0001)
#          pyautogui.click(1041,935)
        break
