import json, requests
from xlwt import *

url = "http://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()

for i in data["followers"]:
    print(i)

#print(data)