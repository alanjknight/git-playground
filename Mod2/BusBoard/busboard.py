#transport key: 224b784d3583e78b37e4b5187209c7cd
#app ID:        f36238d0

import requests
 
resp = requests.get("https://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=f36238d0&app_key=224b784d3583e78b37e4b5187209c7cd&group=no&nextbuses=yes")


json = resp.json()

#print(json['departures']['all'])

for bus in json['departures']['all']:
    print("line:"+bus['line'])
    print("direction:"+bus['direction'])

# typing 

