
from bs4 import BeautifulSoup


with open("../Week 2/2.9.2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())
