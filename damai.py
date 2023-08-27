#coding=utf-8

import os
if os.name=='nt':
    import pyautogui
import time
from pymouse import PyMouse
import random

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
        if os.name=='nt':
            os.system('cls')
        elif os.name=='posix':
            os.system('clear')
        if time.strftime("%H:%M:%S")==start:
            now=time.time()
            while time.time()-now<=int(duration):
                if os.name=='nt':
                    m.click(1150,935,1)#windows中的位置 
#              pyautogui.click(1150,935,duration=0.0001)
#              pyautogui.click(1041,935)
                elif os.name=='posix':
                    x=random.randint(763,814)
                    y=random.randint(667,692)
                    m.click(x,y,1)#linux
                    time.sleep(0.12)
            break
