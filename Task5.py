import requests
import json
from Task1 import scrape_top_list
from Task4 import movie_details
movie_data=scrape_top_list()
def get_movie_list_details():
    list=[]
    for i in movie_data:
        k=i["url"]
        # print(k)
        a=movie_details(k)
        # print(a)
        list.append(a)
        # print(list)
    with open("task5.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
        
get_movie_list_details()