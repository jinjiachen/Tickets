#!/bin/python
#coding=utf8
'''
Author: Michael Jin
Date: 2024-04-20
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import urllib
import requests
import os
import time

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
    #driver.set_page_load_timeout(10)
    #driver.set_script_timeout(10)
    print('starting')
    return driver


def ssky():
    #手动登录
    login_url='https://www.ssky123.com/online_booking_pc/#/login'
    driver.get(login_url)
    input('请登录，登录后按任意键继续！')


    url='https://www.ssky123.com/online_booking_pc/#/index'
    driver.get(url)
    time.sleep(3)

    #以下是出发和到达港口的选择
    driver.find_element(By.XPATH,'//div[@class="index__content"]/div[@class="row index__place"][1]/div[1]').click()
    driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[1]/div/div/div[7]').click()
    driver.find_element(By.XPATH,'//div[@style="display: flex; width: 100%;"]/div[2]/div/div[2]').click()

    #选择时间
    driver.find_element(By.XPATH,'//div[@class="row index__date"]/div[1]/p[2]').click()
    driver.find_element(By.XPATH,'//div[@class="wh_content"][2]/div[30]').click()

    #开始查询
    driver.find_element(By.XPATH,'//div[@class="row index__search"]//button').click()

    #booking
    time.sleep(1)
    driver.find_element(By.XPATH,'//div[@class="list__content"]/div/p[8]/span').click()


    #添加联系人
#    driver.find_element(By.XPATH,'//div[@style="background: rgb(244, 244, 244); margin-top: 10px;"]/p[2]/div/div').click()
    driver.find_element(By.XPATH,'//div[@class="q-option cursor-pointer no-outline row inline no-wrap items-center selectperson q-checkbox q-focusable"]').click()
#    driver.find_element(By.XPATH,'//div[@style="background: rgb(244, 244, 244); margin-top: 10px;"]/p[2]/div//input').click()
#    driver.find_element(By.XPATH,'//i[@class="q-icon q-checkbox-icon cursor-pointer material-icons"][1]').click()

    #下单
    driver.find_element(By.XPATH,'//div[@style="padding-left: 216px; margin-top: 20px;"]//button').click()




if __name__ == '__main__':
    driver=Driver()
    ssky()
