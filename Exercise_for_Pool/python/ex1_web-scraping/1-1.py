#!/usr/bin/env python3

import requests, re
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://r.gnavi.co.jp/area/aream2105/rs/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

restraunts = soup.find_all(class_="style_titleLink__oiHVJ")
f = open("output.txt", "w")
for r in restraunts:
    f.write(r.getText())
    f.write(':')
    f.write(r.get('href'))
    f.write("\n")

'''
f = open("output.txt", "w")
    f.write(str(link.get('href')))

for restaurant in restaurants:
    restaurant_url = restaurant.find('href')
    f = open("output.txt", "w")
    f.write(str(restaurant_url.prettify()))
    f.close()
print("done")
'''
