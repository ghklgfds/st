import pandas as pd
import streamlit as st
a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.title('有効求人倍率統計')
st.write(a)
st.text(a.columns)
for i in  a:
   c=i['時点'].find('2021年7')
   if c>-1:
      st.text(i)
      
   
