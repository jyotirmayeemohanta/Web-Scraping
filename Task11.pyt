import json
import requests
# from bs4 BeautifulStoneSoup
with open("Task5.json","r+") as file:
    data2=json.load(file)
# print(data2)
def analyse_movies_genre():
    gener_list={}
    for i in data2:
        if "genre" in i:
            Genre=i["genre"]
            for i in Genre:
                if i not in gener_list:
                    gener_list[i]=1
                else:
                    gener_list[i]+=1
    print(gener_list)
    with open("Task11.json","w+") as file1:
        json.dump(gener_list,file1,indent=4)

analyse_movies_genre()

