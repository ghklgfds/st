

import requests
import pandas as pd
import json
import streamlit as st
import time 
import datetime



def stitle(tank,selecttitle):

    for t in tank:
      cnt=1
    
      n=selecttitle
      #st.text(n)
      if t[2]==n:
         #st.text(t[2])
         return t[2]
        
@st.cache
def sact(tank,acttank):
    
    for v in tank:
      cnt=1
      if selectact!='':
       p=selectact
    
       if v[5]==p :
          return v[5]
        






if 'value' not in st.session_state:
    st.session_state['value'] = 'True'





f = open('Key.txt', 'r', encoding='UTF-8')

key = f.read()


f.close()

now = datetime.datetime.now()
if now.month<10:
    month=str(0)+str(now.month)
else:
    month=str(now.month)
#st.text(now.month)
#import streamlit as st
#mon = st.slider('何月?', 1, 12, 9)
st.write('私の書評ブログです。ぜひ来てください。')
st.write('https://www.a-littlegoodbooks.com')
st.title('NHKの番組を探す')
if now.day+1>31:
    maxday=now.day+15-31
else :
    maxday=now.day+15
#nowday=now.day
day = st.slider('何日の番組をお探しですか？', now.day, maxday,now.day)
url=('https://api.nhk.or.jp/v2/pg/list/130/g1/2021-'+month+'-'+str(day)+'.json?key=')
a=requests.get(url+key)
mes=(a.text)
if len(mes)<53:
   st.text('番組情報がまだありません。')
elif len(mes)>53:
 b = a.json()
#st.text(b)
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
 titles=df[2]
 acts=df[5]    
 acttank=[]
 for actdata in acts:
    if actdata!='':
        acttank.append(actdata)
 #selectmethod=st.sidebar.radio('method',('タイトル検索','出演者検索'))


 st.session_state['value'] = st.checkbox('出演者検索に切り替えますか？', key='my_checkbox')
 
 if  st.session_state['value']==['True']:
        selectact=st.sidebar.radio(acttank)
        v=sact(tank,selectact)
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

 else:
        
        st.write('番組情報')
        st.text(titles)
        selecttitle=st.sidebar.radio(titles)
        st.text(selecttitle)
        t=stitle(tank,selecttitle)
        for l in t:
           if cnt==1:
              st.write('開始時間')
              st.write(l)
              cnt=cnt+1
           elif cnt==2:
              st.write('終了時間')
              st.write(l) 
              cnt=cnt+1
           elif cnt==3:
              st.write('タイトル')
              st.write(l)
              cnt=cnt+1
           elif cnt==4:
              st.write('サブタイトル')
              st.write(l)
              cnt=cnt+1
           elif cnt==5:
              st.write('概要')
              st.write(l)
              cnt=cnt+1
           elif cnt==6:
              st.write('出演者')
              st.write(l)
              cnt=0



 
