import requests
import json

r = requests.get("https://api.opendota.com/api/players/107828036/matches")

with open('output.json', 'w') as out:
    json.dump(r.json(), out, sort_keys=True, indent='\t')
