import sqlite3
import re
import requests

requests.packages.urllib3.disable_warnings()
conn=sqlite3.connect('train.sqlite')
cur=conn.cursor()

cur.execute('''
DROP TABLE IF EXISTs stations ''')

cur.execute('''
CREATE TABLE stations ( name TEXT, abbreviation varchar(20))''' )

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
r = requests.get(url,verify=False)
pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
result = re.findall(pattern,r.text)
station = dict(result)


for name , abbreviation in station.items() :
    cur.execute('''INSERT INTO stations (name,abbreviation)
                 VALUES (?,?)''', (name,abbreviation))
conn.commit()                
                


