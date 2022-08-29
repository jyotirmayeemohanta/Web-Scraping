# import requests
# from bs4 import BeautifulSoup
# import json

# def  analyse_movies_language(movies_list):




# analyse_movies_language()


from Task5 import*
import json
with open("Task5.json","r") as file:
    b=json.load(file)
def movies_language(k):
    dic= {}
    for i in k:
        if "language" in i:
            m=i["language"]
            for j in m:
                if j in dic:
                    dic[j]=dic[j]+1
                if j not in dic:
                    dic[j]=1
    with open("task6.json","w+") as file:
        json.dump(dic,file,indent=4)
    # return dic

movies_language(b)


