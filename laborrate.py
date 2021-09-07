import pandas as pd
import streamlit as st
a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.write(a)
st.text(a.columns)
for i in a:
  if i['時点']==['2021年7月']:
    st.text(i)
    
