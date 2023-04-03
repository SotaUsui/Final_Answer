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
count =0
i=0
page =1
while count < 50:
    s_url = elements[i].get_attribute("href")
    url_list.append(s_url)
    count +=1
    i +=1
    if i == 20:
        page +=1
        n_url =url+"&p="+str(page)
        driver.get(n_url)
        elements = driver.find_elements(By.CLASS_NAME, "style_titleLink__oiHVJ")
        i =0

name =[]
phone =[]
email =[]
prefecture =[]
city = []
address =[]
building =[]
own_url =[]
ssl =[]

for store in url_list:
    driver.get(store)
    #name
    store_name = driver.find_element(By.ID, "info-name").text
    name.append(store_name)

    #phone
    store_phone = driver.find_element(By.CLASS_NAME, "number").text
    print(store_phone)
    phone.append(store_phone)



driver.close()
driver.quit()
