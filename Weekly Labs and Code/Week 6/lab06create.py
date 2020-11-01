import requests

import json

dataString = {'make':'Ford','model':'Cougar', 'reg':'01KY1', 'price':'14000'}
url = "http://127.0.0.1:5000/cars"


response = requests.post(url, json=dataString)

print(response.status_code, response.text)

