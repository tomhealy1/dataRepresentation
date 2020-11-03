import requests
import json
 
url = "https://prodapi.metweb.ie/observations/valentia/today"

response = requests.get(url)
data = response.json()

print(data)
for row in data:
    print(row["pressure"])



#filename = 'weather031120.json'

#f = open(filename, 'w')
#json.dump(data, f, indent=4)