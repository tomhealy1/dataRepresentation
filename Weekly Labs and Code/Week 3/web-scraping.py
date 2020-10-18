import requests
import csv
from bs4 import BeautifulSoup
import numpy as np
#homepage to scrape

pages = np.arange(1, 5, 1)

for page in pages: 
  
    page = requests.get("https://www.myhome.ie/residential/kerry/property-for-sale?page=" + str(page))

#url = "https://www.myhome.ie/residential/kerry/property-for-sale?page=1"
#page = requests.get(url)
#pass the content to the var soup
soup = BeautifulSoup(page.content, 'html.parser')

#Open a file called week03MyHomeFun.csv in write mode :
home_file = open('week03MyHomeFun2.csv', mode ='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings =soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()



