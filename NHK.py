

import requests
import pandas as pd
import json
import streamlit as st
import time 
import datetime



def stitle(tank,titles):
    #titles.insert(0, '出演者で検索')
    st.write('番組情報')
    #st.text(titles)
    cnt=1
    selecttitle=st.sidebar.radio('タイトル',titles)
    st.text(selecttitle)
    
    for t in tank:
      cnt=1
    
      n=selecttitle
      
      st.text(n)
      if t[2]==n:
        st.text(t[2])
        st.write('番組情報')
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
      
        

def sact(tank,acttank):
    selectact=st.sidebar.radio('出演者',acttank)
    for v in tank:
      cnt=1
      if selectact!='':
       p=selectact
    
       if v[5]==p :
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
        








tank=[]
f = open('Key.txt', 'r', encoding='UTF-8')

key = f.read()


f.close()
now = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)
#now = datetime.datetime.now()
#st.text(now)
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
selectchannel=st.radio('チャンネルを選んでください',('総合','Eテレ','BS1','BSプレミアム','ＮＨＫラジオ第1','ＮＨＫラジオ第2','ＮＨＫＦＭ'))
if selectchannel=='総合':
        channel='g1'
elif  selectchannel=='Eテレ':
        channel='e1'
elif  selectchannel=='BS1':
        channel='s1'
elif  selectchannel=='BSプレミアム':
        channel='s3'
elif  selectchannel=='ＮＨＫラジオ第1':
        channel='r1'
elif  selectchannel=='ＮＨＫラジオ第2':
        channel='r2'
elif  selectchannel=='ＮＨＫＦＭ':
        channel='r3'
elif  selectchannel=='ＮＨＫラジオ第1':
        channel='r1'

 
       
nowday=now.day
day = st.slider('何日の番組をお探しですか？', 1, 31,nowday)
#st.text(nowday)
if int(day)<10:
    url=('https://api.nhk.or.jp/v2/pg/list/130/'+channel+'/2022-'+str(month)+'-0'+str(day)+'.json?key=')
    st.text(day)
else:
    url=('https://api.nhk.or.jp/v2/pg/list/130/'+channel+'/2022-'+str(month)+'-'+str(day)+'.json?key=')
    st.text(day)
 

#url=('https://api.nhk.or.jp/v2/pg/list/130/g1/0000/2021-'+str(month)+'-'+str(day)+'.json?key=')
#url=('https://api.nhk.or.jp/v2/pg/list/130/g1/0000/2021-11-01.json?key=')
a=requests.get(url+key)
mes=(a.text)
#st.text(url)
#st.text(len(mes))
if len(mes)==51:
   st.text('番組情報がまだありません。')
   
elif len(mes)!=51:
 b = a.json()
 st.text(b)
 c=(b['list'][channel])

 tank=[]
 for i in c:
    for m in i:
        print(m)
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
 print(tank)
 df=pd.DataFrame(tank)
 titles=df[2]
 acts=df[5]    
 acttank=[]
 for actdata in acts:
        if actdata!='':
           acttank.append(actdata)
 



selectmethod=st.radio('検索方法を選んでください',('タイトル検索','出演者検索'))
st.text(len(selectmethod))
if len(selectmethod)==6:
    if tank!=[]:
       stitle(tank,titles)
elif len(selectmethod)==5:
    if tank!=[]:
       sact(tank,acttank)
st.write("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[PR]━┓
　高速・多機能・高安定レンタルサーバー『エックスサーバー』
　─────────────────────────────────
 ・月額990円(税込)から、大容量300GBからの高コストパフォーマンス
 ・安定のサーバー稼働率99.99％以上
 ・高速性を重視し、最新48コアCPU＋大容量512GBメモリ＋
　 「オールNVMe」RAID10構成を採用！
 ・幅広いバージョンのPHPやSSHに対応！
 ・初心者でも安心の24時間365日メールサポート！
　─────────────────────────────────
　　https://px.a8.net/svt/ejp?a8mat=3HOOWF+C7ZI8A+CO4+5ZU2B
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")



 
        
        
        
        



 
