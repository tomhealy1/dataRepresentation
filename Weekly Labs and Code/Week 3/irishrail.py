import requests
import csv
from bs4 import BeautifulSoup

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

soup = BeautifulSoup(page.content, 'xml')

##print(soup.prettify())

listings = soup.findAll("objTrainPositions")


with open ('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    listings = soup.findAll("objTrainPositions")   
    for listing in listings:
        lat =float(listing.TrainLatitude.string)
        if (lat < 53.4):

    #print(listing)
        #print(listing.find('TrainLatitude').string)
            entryList = []
            for retrieveTag in retrieveTags:

                entryList.append(listing.find('TrainLatitude').string)
        train_writer.writerow(entryList)
