

import requests
import pandas as pd
import bs4
import json
import streamlit as st
url=('https://api.nhk.or.jp/v2/pg/list/130/g1/2021-09-13.json?key=')
key='lMA29WCIfOF57Gvt5cGi84Ee4RTsI97r'
a=requests.get(url+key)

b = a.json()
c=(b['list']['g1'])
tank=[]
for i in c:
    for m in i:
        print(m)
    start=i['start_time']
    end=i['end_time']
    area=i['area']
    service=i['service']
    title=(i['title'])
    subtitle=(i['subtitle'])
    content=(i['content'])
    act=i['act']
    genres=i['genres']
    data=[start,end,area,service,title,subtitle,content,act,genres]
    tank.append(data)
df=pd.DataFrame(tank)
st.write(df)
#df.to_csv('nhk.csv')
    



