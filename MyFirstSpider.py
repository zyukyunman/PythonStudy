# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = "https://nba.hupu.com"
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,'html.parser')
image = soup.select('img')
news = soup.select('dd') 
for i in news:
    a = i.select('a[title]')
    b = i.select('a[href="https://bbs.hupu.com/20993526.html"]')
    c = i.select('a[href="https://bbs.hupu.com/20985034.html"]')
    if (len(a) >0 or len(b) > 0 or len(c) > 0):
      continue
    h = i.select('a')[0].text
    href = i.select('a')[0]['href']
    like = i.text.split()
    if len(like) > 1 :
       site = {"name": h, "url": href, "like": like[1]}
       print("新闻：{name}, 地址:{url} {like}".format(**site))
    else :
       site = {"name": h, "url": href}
       print("新闻：{name}, 地址:{url}".format(**site))