import requests
import csv
from bs4 import BeautifulSoup


page = requests.get("https://tomhealy1.github.io/")

soup1 = BeautifulSoup(page.content, 'html.parser')

print(page)

print("----------------")

print(soup1.prettify())
