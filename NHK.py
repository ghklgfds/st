

import requests
import pandas as pd
import json
import streamlit as st
import time 
import datetime
now = datetime.datetime.now()
#import streamlit as st
#mon = st.slider('何月?', 1, 12, 9)
st.title('NHKの出演者から番組を探す')
day = st.slider('何日?', now.day, now.day+7,now.day)
url=('https://api.nhk.or.jp/v2/pg/list/130/g1/2021-09-'+str(day)+'.json?key=')
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
    data=[starttime,endtime,title,subtitle,content,act]
    tank.append(data)
#print(tank)
df=pd.DataFrame(tank)

                          
acts=df[5]    
acttank=[]
for actdata in acts:
    if actdata!='':
        acttank.append(actdata)

titles=df[3]

selecttitle=st.sidebar.selectbox('select',(titles))
if selecttitle=='':   
 selectact= st.sidebar.selectbox("チェックした出演者の番組情報を入手できます",(acttank))
for v in tank:
    cnt=1
    if selectact!='':
       p=selectact
    
       if v[5]==p :
        st.write('番組情報')
        
        for u in v:
           if cnt==1:
              st.write('開始時間')
              st.write(u)
              cnt=cnt+1
           elif cnt==2:
              st.write('終了時間')
              st.write(u) 
              cnt=cnt+1
           elif cnt==3:
              st.write('タイトル')
              st.write(u)
              cnt=cnt+1
           elif cnt==4:
              st.write('サブタイトル')
              st.write(u)
              cnt=cnt+1
           elif cnt==5:
              st.write('概要')
              st.write(u)
              cnt=cnt+1
           elif cnt==6:
              st.write('出演者')
              st.write(u)
              cnt=0
                
for t in tank:
    cnt=1
    
    n=selectitle
    
    if v[5]==n:
        st.write('番組情報')
        
        for u in v:
           if cnt==1:
              st.write('開始時間')
              st.write(u)
              cnt=cnt+1
           elif cnt==2:
              st.write('終了時間')
              st.write(u) 
              cnt=cnt+1
           elif cnt==3:
              st.write('タイトル')
              st.write(u)
              cnt=cnt+1
           elif cnt==4:
              st.write('サブタイトル')
              st.write(u)
              cnt=cnt+1
           elif cnt==5:
              st.write('概要')
              st.write(u)
              cnt=cnt+1
           elif cnt==6:
              st.write('出演者')
              st.write(u)
              cnt=0
