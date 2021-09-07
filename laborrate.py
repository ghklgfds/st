import pandas as pd
import streamlit as st
a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.title('有効求人倍率統計')
st.write(a)
st.text(a.columns)
for i in a['時点']:
   b=list(i)
   c=list('20217')
   d=len(set(b&c))
   if d==5:
      st.text(i)
