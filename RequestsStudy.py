# -*- coding: utf-8 -*-
import requests

# 请求及传递URL参数
# url = "https://nba.hupu.com/get"
# kv  = {'k':'v','k1':'v1'}
# r = requests.get(url,params=kv)
# print(r.url)

# 响应内容
r = requests.get('https://github.com/timeline.json')
# print(r.encoding)
# r.encoding = 'ISO-8859-1'
# print(r.encoding)
# print(r.text)
# r.json()
# print(r)

from PIL import Image
from io import BytesIO
# 二进制响应
# url = "https://w1.hoopchina.com.cn/22/10/b1/2210b1a332f3bbd8caefbaec6770f253002.png"
# r = requests.post(url)
# print(r.text)
# print(r.headers)
# i = Image.open(BytesIO(r.content))

# cookie
# url = "https://nba.hupu.com/post"
# print(r.cookies['stream-nba-13'])