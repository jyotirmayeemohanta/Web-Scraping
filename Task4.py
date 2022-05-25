# import requests
# from bs4 import BeautifulSoup
# import json

# from Task1 import scrape_top_list

# url ="https://www.rottentomatoes.com/m/pinocchio_1940"
# # print(url)

# def movie_details():
#     data=requests.get(url)
#     soup = BeautifulSoup(data.text,"html.parser") 
#     # print(soup)
#     main_li=soup.find_all("li ",class_="meta-row clearfix")
#     # print(main_li)
#     name=soup.find("h1",class_="scoreboard__title").get_text()
#     # print(name)
#     dict={}
#     for i in main_li:
#         k=i.text
#         n=k.split()
#         print(n)
#         for j in n:
#             if "Rating" in j:
#                 dict["name"]=name
#                 dict["Rating"]=n[1]
            
#             if "Genre" in j:
#                 a=n[1:]
#                 n=""
#                 for i in a:


# movie_details() 



import requests
import json
from bs4 import BeautifulSoup

url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def movie_details(url):
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")

    dict={}
    div=soup.find("div",class_="container")
    body=div.find("div", class_="media-body")
    li=body.find_all("li")

    # bio=body.find("div", id="movieSynopsis").get_text().strip()
    # dict["bio"]=bio
    movie_name=div.find("h1", slot="title").get_text()
    dict["movie_name"]=movie_name

    for i in li:
        data=i.text
        a=data.split()
        if "Rating:" in a:
            dict["rating"] = a[1:2]
        if "Runtime:" in a:
            b=a[1:]
            for j in range(len(b)):
                if "h" in b[j]:
                    hour=int(b[j][:-1])*60
                elif "m" in b[j]:
                    min=int(b[j][:-1])
            time=hour+min
            dict["runtime"] = time
        if "Language:" in a:
            dict["language"]=a[2:]
        if "Director:" in a:
            # c=a[1:]
            a1=a[1:] 
            d=""
            for k in a1:
                d+=k
            d=d.split(",")
            dict["director"] = d
        if "Genre:" in a:
            c=a[1:]
            s=" "
            for l in c:
                s+=l
            s=s.strip()
            s=s.split(",")

        
            dict["genre"] = s
        
    with open("Task4.json","w+") as file:
        json.dump(dict , file, indent=4)
    return dict    
movie_details(url)