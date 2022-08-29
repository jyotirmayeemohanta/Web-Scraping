from asyncio import Task
import json
import requests
from bs4 import BeautifulSoup
from Task4 import movie_details
from Task12 import movie_actor_details
url="https://www.rottentomatoes.com/m/coco_2017"
def final_movie(url1):
    list=[]
    Task4=movie_details(url1)
    Task12=movie_actor_details(url1)
    Task4["cast"]=12
    list.append(Task4)
    with open("Task13.json","w+") as file1:
        json.dump(list,file1,indent=4)
        print(list)
final_movie(url)