from pprint import pprint
import requests,json,os
try:
    if os.path.exists("api.json"):
        f=open("api.json",'r')
        json_data=json.load(f)
    else:
        res=requests.get("http://saral.navgurukul.org/api/courses").text
        json_data=json.loads(res)
        f=open("api.json",'w')
        json.dump(json_data,f,indent=4)
        f.close()
finally:
    num=1
    list1=[]
    id_list=[]
    for i in (json_data['availableCourses']):
        num=str(num)
        course=(num+'. '+i['name'])
        print(course)
        list1.append(course)
        num=int(num)
        num+=1
        id1=i['id']
        id_list.append(id1)
    inp=int(input("choose your  course\n"))
    inp-=1
    print(list1[inp])
    idd=id_list[inp]
    new_url=requests.get("http://saral.navgurukul.org/api/courses/"+idd+"/exercises")
    w=new_url.text
    war=json.loads(w)
    b=war['data']
    num=1
    list2=[]
    for j in b:
        list3=[]
        int_slugs="http://saral.navgurukul.org/api/courses/"+(idd)+"/exercise/getBySlug?slug="+j['slug']
        dr=str(num)+"."+j['name']
        num=int(num)
        print (dr)
        list3.append(int_slugs)
        j=j['childExercises']
        num1=1
        for k in j:
            z=str(num)+'.'+str(num1)
            print('  '+z, k['name']  )
            float_slugs="http://saral.navgurukul.org/api/courses/"+(idd)+"/exercise/getBySlug?slug="+k['slug']
            dic={z:float_slugs}
            list3.append(float_slugs)
            list2.append(dic)
            num1+=1
        dic2={num:list3}
        list2.append(dic2)
        num+=1
    n=input('enter any sequence')
    for i in list2:
        for j in i:
            try:
                if n==j:
                    res=requests.get(i[j]).text
                    res=json.loads(res)
                    p=(res['content'])
                    p=json.loads(p)
                    print(p[0]['value'])
                if int(n)==j:
                    c=0
                    for x in i[j]:
                        res=requests.get(x).text
                        res=json.loads(res)
                        p=(res['content'])
                        p=json.loads(p)
                        print(str(c)+'. ', p[0]['value'])
                        c+=1
            except:
                pass