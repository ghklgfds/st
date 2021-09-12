

import requests
import pandas as pd
import json
import streamlit as st
import time 
#import streamlit as st
#mon = st.slider('何月?', 1, 12, 9)
st.title('NHKの出演者から番組を探す')
day = st.slider('何日?', 1, 31, 15)
url=('https://api.nhk.or.jp/v2/pg/list/130/g1/2021-09-'+str(day-1)+'.json?key=')
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

                          
acts=df[6]       
                    
                    


selectact = st.radio("お好みの出演者から番組情報を入手できます",(acts))
for v in tank:
    cnt=0
    num=0
    p=selectact
    if v[6]==p:
        st.write('番組情報')
        for u in v:
           
           st.write(u)
                    
    num=num+1

