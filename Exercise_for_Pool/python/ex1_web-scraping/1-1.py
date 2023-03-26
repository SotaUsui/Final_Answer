#!/usr/bin/env python3

import requests, re, time
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://r.gnavi.co.jp/area/aream2105/rs/'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
header = {
    'User-Agent': user_agent
}
time.sleep(3)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
restraunts = soup.find_all(class_="style_titleLink__oiHVJ")

url_list = []
count =0
i =0

while(count < 50):
    url_list.append(restraunts[i].get('href'))
    count +=1
    i +=1
    if (i == len(restraunts)):
        pages = soup.find(class_="style_pages__Y9bbR")
        page =(pages.find_all('a'))
        next_page = (page[9].get('href')) #I though it was 7 not 9.
        next_page = "https://r.gnavi.co.jp"+next_page
        response = requests.get(next_page)
        soup = BeautifulSoup(response.text, 'html.parser')
        restraunts = soup.find_all(class_="style_titleLink__oiHVJ")
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

for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #name
    store_name = soup.find(class_ = 'fn org summary')
    store_name = store_name.text
    store_name = re.sub(r'\xa0', '', store_name)
    name.append(store_name)

    #phone
    store_phone = soup.find(class_ = 'number')
    store_phone = store_phone.text
    phone.append(store_phone)

    #email
    email.append("") #I couldn't find any class of email
    
    #prefecture/city/address
    place = soup.find(class_ = 'region')
    place = place.text
    pattern = r"^(.+?[都道府県])(.+?[市区町村])(.+)$"
    match = re.match(pattern, place)
    prefecture.append(match.group(1))
    city.append(match.group(2))
    address.append(match.group(3))

    #building
    store_building = soup.find(class_ = 'locality')

    if store_building == None:
        building.append('')
    else:
        store_building = store_building.text
        building.append(store_building)

    #own_url
    own_url.append("")

    #ssl
    ssl.append("")



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
df.to_csv("1-1.csv", index=False)
