import requests
import pandas as pd
import sys
import numpy as np
import os
import csv
import time
import json
from tomorrow import threads
headers = {
    "Accept": "*/*",
    "cache-control": "max-age=0",

    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
}


@threads(6)
def getaddress(url):
    try:
        # timeout这个参数很有必要，加入你不慎去访问google等我国禁止的网站，那么程序在尝试0.7秒钟连接不上的时候，那么会放弃
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
            return response
        else:
            print(url.status_code)
    except:
        time.sleep(10)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
        except:
            print("time out")


Word = list()
tran = list()
字典 = dict()
f = open('单词词汇.csv', encoding='utf-8')
data = pd.read_csv(f)
Explanation = str()
# 必应词典 API + ?+Word = key  就会返回值
url = "http://xtk.azurewebsites.net/BingDictService.aspx?Word="
# http://xtk.azurewebsites.net/BingDictService.aspx?  例如这样的
k = 0
o = 0
for i in data.ix[:, '单词']:
    Word.append(url + i)
for j in Word:
    url = getaddress(j)
    url.encoding = 'utf-8'
    Z = json.loads(url.text)
    if Z["defs"] is None:
        continue
    for i in Z["defs"]:
        Explanation = ' '
        Explanation += i['def']
    tran.append(Explanation)
    print(tran[k], k)
    字典[Z["word"]] = tran[k]
    k += 1
df = pd.DataFrame(字典, index=[0])
print(df)
df.to_csv('good.csv')
# f['tran'] = df
