#!/bin/python
#coding=utf8
'''
Author: Michael Jin
Date: 2024-04-20
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
from lxml import etree
import urllib
import requests
import os
import time
from notification import notify
from notification import load_config


def Driver():
    #Chrom的配置
    options = webdriver.ChromeOptions()
#    options.add_argument("--proxy-server=http://192.168.2.108:8889")
#    options.add_argument("--no-proxy-server")
#    options.add_argument("--headless")
#    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"')
#    options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"')
#    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36')
    options.add_argument('log-level=3') #INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
#    Chrome的驱动和路径
#    path="C:\Program Files\Google\Chrome\Application\chrome.exe"
#    driver=webdriver.Chrome(chrome_options=options,executable_path=path)
#    driver=webdriver.Chrome(path,chrome_options=options)
    driver=webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    #driver.set_page_load_timeout(10)
    #driver.set_script_timeout(10)
    print('starting')
    return driver


def ssky():
    #手动登录
    login_url='https://www.ssky123.com/online_booking_pc/#/login'
    driver.get(login_url)
#    input('请登录，登录后按任意键继续！')

    #定时
    start=input('请输入开始运行的时间(HH:MM:SS)')
    while True:
        print(time.strftime("%H:%M:%S"))
        if time.strftime("%H:%M:%S")==start:
            time.sleep(0.8)#延迟0.2s
            break

    #自动登录
    conf=load_config()
    username=conf.get('ssky','user')
    passwd=conf.get('ssky','passwd')
    driver.find_element(By.XPATH,'//input[@type="text"]').send_keys(username)
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys(passwd)
    button=driver.find_element(By.XPATH,'//button[@type="button"]').click()

    
    #开始查询订票信息
    url='https://www.ssky123.com/online_booking_pc/#/index'
    driver.get(url)
    time.sleep(1)

    #以下是出发和到达港口的选择
    while True:
        try:
            driver.find_element(By.XPATH,'//div[@class="index__content"]/div[@class="row index__place"][1]/div[1]').click()
            driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[1]/div/div/div[7]').click()
#            driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[2]/div/div[2]').click()#到达：shengshan
#            driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[2]/div/div[1]').click()#到达：sijiao
            driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[2]/div/div[3]').click()#到达：枸杞
            print('港口选择完毕')
            break
        except:
            print('重新选择港口信息!')
            driver.refresh()
            time.sleep(2)


    #选择时间
    while True:
        try:
            driver.find_element(By.XPATH,'//div[@class="row index__date"]/div[1]/p[2]').click()
#            driver.find_element(By.XPATH,'//div[@class="wh_content"][2]/div[36]').click()
            driver.find_element(By.XPATH,'//div[@class="wh_content"][2]/div[38]').click()#5.3
            break
        except:
            print('重新选择时间!')
            driver.refresh()


    #开始查询
    while True:
        try:
            driver.find_element(By.XPATH,'//div[@class="row index__search"]//button').click()
            break
            print('开始查询!')
        except:
            print('重新查询!')


    #booking
    time.sleep(1)
    driver.find_element(By.XPATH,'//div[@class="list__content"]/div[1]/p[8]/span').click()#div[1]为第一个航班


    url='https://www.ssky123.com/online_booking_pc/#/info'
    driver.get(url)
    time.sleep(1)
    #选择仓位
    driver.find_element(By.XPATH,'//div[@class="selectport"]/div/div[1]//span').click()#div[1]为第一个舱位
    #添加联系人
    driver.find_element(By.XPATH,'//div[@class="q-option cursor-pointer no-outline row inline no-wrap items-center selectperson q-checkbox q-focusable"]//span').click()#第一个联系人
    driver.find_element(By.XPATH,'//p[@style="display: inline-block; padding: 8px 10px; margin: 0px;"][2]//span').click()#第二个联系人
#    selector=etree.HTML(driver.page_source)
#    print(driver.page_source)


    #下单
    time.sleep(1)
    driver.find_element(By.XPATH,'//div[@style="padding-left: 216px; margin-top: 20px;"]//button').click()


    #使用模拟点击的方式确认订单
    pyautogui.press('f')#取消mplayer全屏
#    pyautogui.click(1651,672,duration=0.2)#如果仓位满候补的情况下的弹窗
    pyautogui.click(1384,917,duration=0.2)#向下滚动
    pyautogui.click(1384,917,duration=0.2)#向下滚动
    pyautogui.click(1018,907,duration=0.2)#核对信息弹窗确定按钮


    #判断订单是否成功，成功则获取信息
    time.sleep(5)
    current_url=driver.current_url
    print('当前网址：',current_url)
    html=driver.page_source
    selector=etree.HTML(html)
#    print(driver.page_source)
    order=selector.xpath('//div[@style="margin-top: 20px; margin-bottom: 20px; padding: 31px 64px; height: 686px; background: rgb(255, 255, 255);"]/div[1]/div//text()')
    print(order)
    notify('get','ssky',''.join(order))




if __name__ == '__main__':
    driver=Driver()
    ssky()
