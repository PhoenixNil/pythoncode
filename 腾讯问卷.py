from bs4 import BeautifulSoup
import re
import requests
import urllib3
import json
filename = input("请输入文件名\n")
f = open(filename, 'a+')
number = 0
urllib3.disable_warnings()
headers = {
    "Accept": "*/*",
    "cache-control": "max-age=0",

    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
}
# request header
url = requests.get('https://wj.qq.com/sur/get_survey?id=2166945&hash=249f&logger=1&_=1531409586440',
                   headers=headers)  # we need this json!!
url.encoding = 'utf-8'
Data = json.loads(url.text)
del(Data['data']['pages'][0]['questions'][0])  # delate  excess
k = Data['data']['pages'][0]['questions']
for title in k:
    # print(title['title'])
    a = re.findall('[\u4e00-\u9fa5_]', title['title'])
    b = "".join(a)
    number += 1
    if number == 51:
        continue
    else:
        print(number, '.', b)
        question = str(number) + ' .' + b
        f.write(question + '\n')
        if number >= 66:
            break
f.close()
