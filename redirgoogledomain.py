import requests
from bs4 import BeautifulSoup
import socket

#get ip address of google safe search
domain = 'forcesafesearch.google.com'
ip = socket.gethostbyname(domain)

# 发送HTTP GET请求获取网页内容
url = "https://www.fobnotes.com/tools/google-global-country-sites/"  
url2= "https://zhuanlan.zhihu.com/p/83273024" 
response = requests.get(url)
response2 = requests.get(url2)
googledomain=[]
# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有的链接
    links = soup.find_all("a")
    for link in links :
        if "google" in link.get("href")  and len(link.get("href"))<30:
            googledomain.append(link.get("href"))
else:
    print("请求失败，错误代码:", response.status_code)

if response2.status_code == 200:
    soup = BeautifulSoup(response2.content, "html.parser")
    class_element = soup.find(class_="RichText ztext Post-RichText css-1g0fqss")
    # 找到所有的链接
    if class_element:
        # print(class_element.find_all("a"))
        for link in class_element.find_all("a"):
            googledomain.append(link.get("href").replace("https://link.zhihu.com/?target=https%3A//", ""))

else:
    print("请求失败，错误代码:", response.status_code)


address_domin=[f"{ip} "+ element[:-1].replace("https://", "") +" #forcesafesearch" for element in googledomain] #去掉最后的/
sort_merge_address_domin= sorted(list(set(address_domin)))
for i in sort_merge_address_domin:
    print(i)