#coding=utf-8

import pyautogui
import time
import os
from pymouse import PyMouse

###给定目标时间和当前时间，计算剩余时间
def countdown(bell,live):
    '''
    bell(str):如HH:MM:SS
    live(str):如HH:MM:SS
    '''
    data=bell.split(':')#目标时间
    data_live=live.split(':')#实时时间
    if int(data[2])>=int(data_live[2]):
        sec=int(data[2])-int(data_live[2])
        minute=int(data[1])-int(data_live[1])
    elif int(data[2])<int(data_live[2]):
        sec=60+(int(data[2])-int(data_live[2]))#60减去秒差
        minute=int(data[1])-int(data_live[1])-1#分钟-1
    return [minute,sec]

if __name__=='__main__':
    m=PyMouse()
    start=input('开始抢票的时间：')
    duration=input('输入运行时长')
    while True:
        delta=countdown(start,time.strftime('%H:%M:%S'))
        print('当前时间：',time.strftime('%H:%M:%S'))
        print('设定时间：',start)
        print('倒计时：%s分%s秒'%(delta[0],delta[1]))
        os.system('cls')
        if time.strftime("%H:%M:%S")==start:
            now=time.time()
            while time.time()-now<=int(duration):
                m.click(1150,935,1)
#              pyautogui.click(1150,935,duration=0.0001)
#              pyautogui.click(1041,935)
            break
