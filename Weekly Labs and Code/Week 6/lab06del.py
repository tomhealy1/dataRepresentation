import requests

url = "http://127.0.0.1:5000/cars/181%20G%201234"
response = requests.delete(url)

print(response.status_code, response.text)