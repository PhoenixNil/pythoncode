import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

sum = 0
number = 0
xmlurl = 'http://py4e-data.dr-chuck.net/comments_9144.xml'
url = input('Enter localtion ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
for count in counts:
    sum = sum + int(count.text)
    number = number + 1
print('count: ', number)
print('sum: ', sum)
