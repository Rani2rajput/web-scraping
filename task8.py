from task1 import movie_data
import json
import os
import requests
# t1=movie_data()
with open("task1.json","r+")as file:
    a=json.load(file)
def text():
    for i in a:
        path="/home/dell/task8"+i["name"]+".text"
        # path=""+i["movieName"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell/task8"+i["name"]+".text","w")
            # b=open(path,"w")
            url=requests.get(i["link"])
            create1=create.write(url.text)
            create.close()
text()