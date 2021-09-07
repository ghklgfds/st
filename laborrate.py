import pandas as pd
import streamlit as st
a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.title('有効求人倍率統計')
st.write(a)
st.text(a.columns)
for i in a['時点']:
   b=list(i)
   c=list('20217')
   cnt=0
   for x in b:
      for y in c:
         if x==y:
            cnt=cnt+1
   if cnt>3:
      st.text(i)
      
   
