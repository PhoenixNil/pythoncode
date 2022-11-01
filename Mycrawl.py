from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
Count = 0
Sum = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    Count = Count + 1
    Sum = Sum + int(tag.string)
    if Count > 50:
        break
print('Sum=', Sum)
print('Count', Count)
