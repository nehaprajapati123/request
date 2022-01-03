import json
import requests
def req():
    a=requests.get("https://saral.navgurukul.org/api/courses")
    with open("courses.json","w") as file:
        d=json.loads(a.text)
        json.dump(d,file,indent=4)
    with open("courses.json","r") as f:
        data=json.load(f)
    i=0
    id=[]
    while i<len(data["availableCourses"]):
        print(i,">>>",data["availableCourses"][i]["name"],"...",data["availableCourses"][i]["id"])
        id.append(data["availableCourses"][i]["id"])
        i=i+1
    sno=int(input("enter the serial number of your course: "))
    xmex=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[sno])+"/exercises")
    a=xmex.json()
    slug=[]
    k=0
    while k<len(a["data"]):
        print(k,a["data"][k]["name"])
        slug.append(a["data"][k]["slug"])
        k=k+1
    slugno=int(input("enter your slug number"))
    requui=requests.get("http://saral.navgurukul.org/api/courses/"+str(sno)+"/exercise/getBySlug?slug="+slug[slugno])
    qu=requui.json()
    print(qu["content"])
    j=0
    while j<len(slug):
        choose=input("enter what you want to do next from:- up,previous,next,exit>>>  ")
        if choose=="up":
            sluguu=requests.get("http://saral.navgurukul.org/api/courses/"+str(sno)+"/exercise/getBySlug?slug="+slug[slugno-1])
            x=sluguu.json()
            print(slugno-1,"content",x["content"])
        elif choose=="previous":
            sluguu=requests.get("http://saral.navgurukul.org/api/courses/"+str(sno)+"/exercise/getBySlug?slug="+slug[slugno-1])
            y=sluguu.json()
            print(slugno-1,"content",y["content"])
        elif choose=="next":
            sluguu=requests.get("http://saral.navgurukul.org/api/courses/"+str(sno)+"/exercise/getBySlug?slug="+slug[slugno+1])
            z=sluguu.json()
            print(slugno+1,"content",z["content"])
        elif choose=="exit":
            req()
        j=j+1
req()