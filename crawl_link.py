import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
page = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')

while page < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    postion = 1
    for tag in tags:
        postion = postion + 1
        if postion == 19:
            url = tag.get('href', None)
            name = tag.string
            break
    page = page + 1
print(name)
