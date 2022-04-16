import json
from Task1 import scrape_top_list
a=scrape_top_list()


def  group_by_year(movie):
   
    dic={}    
    for i in movie:
        year=i["year"]
        movies=[]
        for j in movie:
            if j["year"]==year:
                movies.append(j)
        dic[year]=movies
  
    # print(dic)
    with open("Task2.json","w+") as file:
        json.dump(dic,file,indent=4)
      
    return dic
year_=group_by_year(a)




