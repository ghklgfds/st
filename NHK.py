

import requests
import pandas as pd
import json
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
for v in tank:
    cnt=0
    num=0
    p='ゆりやん'
    #print(p)
    y=list(p)
    
    x=list(v[6])
    #print([y,q])
    for f in x:
        for g in y:
            if f==g:
                cnt=cnt+1
                if cnt > len(p)*0.8:
                    yuri=(v)
                    
                    
                    
                    
    num=num+1
    
st.text(yuri)
