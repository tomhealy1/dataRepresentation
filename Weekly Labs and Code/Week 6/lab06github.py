import json, requests
from xlwt import *

url = "http://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()

for follower in data:
    print(follower)

#print(data)
#filename = 'githubusers.json'
#with open(filename, 'w') as f:
 #   json.dump(data, f, indent=4)


w = Workbook()
ws = w.add_sheet('github')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"events_url")
ws.write(row,5,"gravatar_id")
ws.write(row,6,"url")
ws.write(row,7,"html_url")
ws.write(row,8,"followers_url")
ws.write(row,9,"following_url")
ws.write(row,10,"gists_url")
ws.write(row,11,"starred_url")
ws.write(row,12,"subscriptions_url")
ws.write(row,13,"organizations_url")
ws.write(row,14,"repos_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row += 1

for follower in data:
    ws.write(row,0,follower["login"])
    ws.write(row,1,follower["id"])
    ws.write(row,2,follower["node_id"])
    ws.write(row,3,follower["avatar_url"])
    ws.write(row,4,follower["events_url"])
    ws.write(row,5,follower["gravatar_id"])
    ws.write(row,6,follower["url"])
    ws.write(row,7,follower["html_url"])
    ws.write(row,8,follower["followers_url"])
    ws.write(row,9,follower["following_url"])
    ws.write(row,10,follower["gists_url"])
    ws.write(row,11,follower["starred_url"])
    ws.write(row,12,follower["subscriptions_url"])
    ws.write(row,13,follower["organizations_url"])
    ws.write(row,14,follower["repos_url"])
    ws.write(row,15,follower["received_events_url"])
    ws.write(row,16,follower["type"])
    ws.write(row,17,follower["site_admin"])
    row+=1

w.save('github1.xls')
