import requests
import requests

url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename="repo.json"


response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)