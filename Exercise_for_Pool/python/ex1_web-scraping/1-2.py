#!/usr/bin/env python3
import re, time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


path = "/Users/usuisota/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path= path)

time.sleep(3)
url ='https://r.gnavi.co.jp/area/jp/western/rs/?date=20230326'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTM    L, like Gecko) Chrome/111.0.0.0 Safari/537.36'
header = {
        'User-Agent': user_agent
        }
driver.get(url)
driver.maximize_window()

elements = driver.find_elements(By.CLASS_NAME, "style_titleLink__oiHVJ")
url_list = []
count =1
i=0
while count < 50:
    url = elements[i].get_attribute("href")
    url_list.append(url)
    count +=1
    i +=1
    if i == 20:
        page_list =driver.find_elements_by_xpath('//ul[@class="style_pages__Y9bbR"]/li')
        print("-------------")
        print(page_list)
        link_next = page_list[9].get_attribute("href")
        link_next.click()
        elements = driver.find_elements(By.CLASS_NAME, "style_titleLink__oiHVJ")
        i =0
print(url_list)
driver.quit()



















driver.close()
driver.quit()
