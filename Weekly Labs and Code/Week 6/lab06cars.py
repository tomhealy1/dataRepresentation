import requests
from xlwt import *
import json

url = "http://127.0.0.1:5000/cars"


response = requests.get(url)
data = response.json()

for car in data["cars"]:
    print(car)
#print(data)

#filename = 'cars.json'
#if filename:
 #   with open(filename, 'w') as f:
  #      json.dump(data, f, indent=4)

#w = Workbook()
#ws = w.add_sheet('cars')
#row = 0;
#ws.write(row,0,"reg")
#ws.write(row,1,"make")
#ws.write(row,2,"model")
#ws.write(row,3,"price")
#row += 1

#for car in data["cars"]:
    #ws.write(row,0,car["reg"])
    #ws.write(row,1,car["make"])
    #ws.write(row,2,car["model"])
    #ws.write(row,3,car["price"])
    #row+=1

#w.save('cars.xls')
