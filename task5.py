import json
from task1 import movie_data
from task4 import movie_details

with open("task1.json","r") as file:
    data=json.load(file)
def get_movie_details_list():
    list1=[]
    for i in data:
        k=i["link"]
        list1.append(movie_details(k))

    with open("task5.json","w") as file5:
        json.dump(list1,file5,indent = 4)
    return list1
get_movie_details_list()