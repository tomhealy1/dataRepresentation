import requests

import json

dataString = {'make':'Ford','model':'Cougar', 'reg':'02KY1'}
url = "http://127.0.0.1:5000/cars/test"


response = requests.put(url, json=dataString)

print(response.status_code, response.text)

