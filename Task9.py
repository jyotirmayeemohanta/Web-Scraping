import os
import random
import time
import requests
import json

from yaml import dump

file = open("Task5.json","r+")
data = json.load(file)
file.close()
def data_txt():
    time_ = random.randint(1,3)
    for i in data:
        path = "/home/admin123/Desktop/task9" + i["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            data_file=open(path,"w+")
            json,dump(i,data_file,indent=4)
        time.sleep(time_)
data_txt()

