#!/usr/bin/env python3

import requests, re
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://r.gnavi.co.jp/area/aream2105/rs/'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
header = {
    'User-Agent': user_agent
}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
restraunts = soup.find_all(class_="style_titleLink__oiHVJ")

r_url = []
count =0
i =0
#f = open("output.txt", "w")
while(count < 50):
    #f.write(restraunts[i].getText())
    #f.write(':')
    #f.write(restraunts[i].get('href'))
    r_url.append(restraunts[i].get('href'))
    #f.write("\n")
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

print(r_url)

name =[]
phone =[]
email =[]
prefecture =[]
city = []
address =[]
building =[]
own_url =[]
ssl =[]

for i in r_url:




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
df.to_csv("1-1.csv", encoding="shift_jis")
