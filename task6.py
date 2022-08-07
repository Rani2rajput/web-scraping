import json
from bs4 import BeautifulSoup
from task5 import get_movie_details_list

language=get_movie_details_list()
def analyse_movies_language(language):
    dict={}
    for i in language:
        language=i["Language"]
        for j in language:
            if j not in i:
                dict[j]=i
            else:
                dict+=1
    print(dict)
    # print(language)
    with open ("task6.json","w+") as file:
        json.dump(dict,file,indent=4)
analyse_movies_language(language)

        
