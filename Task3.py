import json
from Task2  import scrape_top_list

web= scrape_top_list()
def group_by_decade(movies):
    movies_dic={}
    movies_list=[]
    unique_l=[]
    for i in movies:
        for j in i:
            if j=="year":
                if i[j] not in unique_l:
                    unique_l.append(i[j])
    unique_l.sort()
    for i in unique_l:
        modules=int(i)%10
        mod_s=int(i)-modules
        if mod_s not in movies_list:
            movies_list.append(mod_s)
    for x in movies_list:
        movies_dic[x]=[]
    for x in movies_dic:
        for i in movies:
            for j in i:
                if j=="year":
                    mod_add=x+9

        for i in movies:
            for j in i:
                if j=="year":
                    if int(i[j])<=mod_add and int(i[j])>=x:
                        movies_dic[x].append(i)
    with open("Task3.json","w+") as file:
        json.dump(movies_dic,file,indent=6)
    
    return movies_dic
        
group_by_decade(web)


