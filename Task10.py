import json

# from Task7 import movies_director

file=open("Task5.json","r")
movie_details=json.loads(file.read())
# print(movie_details)

def analyse_language_and_directors():
    dic={}
    list=[]
    for i in movie_details:
        for j in i["director"]:
            if j not in list:
                list.append(j)
    # print(movie_details)
    for i in list:
        dic1={}
        for x in movie_details:
            if i in x["director"]:
                if "language" in x:
                    for z in x["language"]:
                        if z in dic1:
                            dic1[z]=dic1[z]+1
                        if z not in dic1:
                            dic1[z]=1
        dic[i]=dic1
    # print(b)
    with open("Task10.json","w+") as file:
        json.dump(dic,file,indent=4)

analyse_language_and_directors()
