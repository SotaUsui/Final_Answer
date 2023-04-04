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
        ul_element = driver.find_element(By.CSS_SELECTOR,'ul.style_pages__Y9bbR')
        li_elements = ul_element.find_elements(By.CSS_SELECTOR, 'li')
        next_page = li_elements[9]
        next_page.click()
        next_url = driver.current_url
        driver.get(next_url)
        elements = driver.find_elements(By.CLASS_NAME, "style_titleLink__oiHVJ")
        i=0

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
    phone.append(store_phone)

    #email
    email.append('')

    #prefecture/city/address
    place = driver.find_element(By.CLASS_NAME, "region").text
    pattern = r"^(.+?[都道府県])(.+?[市区町村])(.+)$"
    match = re.match(pattern, place)
    prefecture.append(match.group(1))
    city.append(match.group(2))
    address.append(match.group(3))

    #building
    try:
        store_building = driver.find_element(By.CLASS_NAME, "locality").text
        building.append(store_building)

    except:
        building.append('')

    #own_url/ssl
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".unit-box.line.cx .clickable a")
        store_url = element.get_attribute("href")
        own_url.append(store_url)
        if store_url.startswith("https://"):
            ssl.append('TRUE')
        else:
            ssl.append('False')
    except:
        own_url.append('')
        ssl.append('')

data = {
        '店舗名': name,
        '電話番号': phone,
        'メールアドレス': email,
        '都道府県': prefecture,
        '市区町村': city,
        '番地': address,
        '建物名': building,
        'URL': own_url,
        'SSL': ssl
        }
df = pd.DataFrame(data)
df.to_csv("1-2.csv", index=False)

driver.close()
driver.quit()
