from bs4 import BeautifulSoup


with open("../Week 2/lab2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#Find first element with tr tag
#print(soup.tr)

#Find all elements with a tag
rows = soup.findAll("tr")
for row in rows:
    #print("------------")
    #print(row)
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print(dataList)


