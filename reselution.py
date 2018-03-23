import urllib.request
import urllib.parse
import urllib.error
import json
count = 0
total = 0
jsonurl = 'http://py4e-data.dr-chuck.net/comments_9145.json'
url = input('input location: ')
print('retrieved ', url)
uh = urllib.request.urlopen(jsonurl)
data = uh.read()
print('Retrieved to ', len(data), 'characters')

info = json.loads(data)
for number in info['comments']:
    total += number['count']
    count += 1
print('count', count)
print('total', total)
