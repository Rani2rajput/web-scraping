import json
from bs4 import BeautifulSoup
from task5 import get_movie_details_list

Directer=get_movie_details_list()
def analyse_movies_director(Directer):
    d={}
    for i in Directer:
        # print(i)
        Directer_name=i["Director"]
        for j in  Directer_name:
            if j not in d:
            
                d[j]=i
            else:
                d[j]+=1
    print(d)
    with open ("task7.json","w") as file:
        json.dump(d,file,indent=4)
    return d
    
analyse_movies_director(Directer)
        
    
