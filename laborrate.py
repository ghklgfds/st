import pandas as pd
import streamlit as st
a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.title('有効求人倍率統計')
st.write(a)
st.text(a.columns)
for (x,y,z) in zip (a['時点'],a['地域'],a['（季節調整値）有効求人倍率【倍】']):
    c=x.find['2021年7月']:
        if c>-1:
            st.text(x+y+z)
   
