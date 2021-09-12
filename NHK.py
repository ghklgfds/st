

import requests
import pandas as pd
import json
import streamlit as st
#import streamlit as st
url=('https://api.nhk.or.jp/v2/pg/list/130/g1/2021-09-13.json?key=')
key='lMA29WCIfOF57Gvt5cGi84Ee4RTsI97r'
a=requests.get(url+key)

b = a.json()
c=(b['list']['g1'])
tank=[]
for i in c:
    #for m in i:
        #print(m)
    start=i['start_time']
    starttime=(start[11:16])
    end=i['end_time']
    endtime=(end[11:16])
    area=i['area']
    service=i['service']
    title=(i['title'])
    subtitle=(i['subtitle'])
    content=(i['content'])
    act=i['act']
    genres=i['genres']
    data=[starttime,endtime,area,title,subtitle,content,act]
    tank.append(data)
#print(tank)
df=pd.DataFrame(tank)

                          
                    
                    
                    
                    
num=num+1
genre = st.radio("What's your favorite movie genre",(tank[6])

for v in tank:
    cnt=0
    num=0
    p='有吉'
    #print(p)
    y=list(p)
    
    x=list(v[6])
    #print([y,q])
    for f in x:
        for g in y:
            if f==g:
                cnt=cnt+1
                if cnt > len(p)*0.9:
                   k=0
                   for d in v:
                      st.text(d)
