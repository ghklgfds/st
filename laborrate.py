import pandas as pd
import streamlit as st

a=pd.read_csv('TimeSeriesResult_20210907231948299.csv')
st.title('有効求人倍率統計')
st.text('全履歴')
st.write(a)
#st.text(a.columns)
tank=[]
tank2=[]
for (x,y,z) in zip (a['時点'],a['地域'],a['（季節調整値）有効求人倍率【倍】']):
    c=x.find('2021年7月')
    if c>-1 and x==x and y==y and z==z:
            d=[x,y,z]
            e=[y,100*z]
            tank.append(d)
            tank2.append(e)
            
df=pd.DataFrame(tank)
df2=pd.DataFrame(tank2)
st.text('2021年7月時点')
st.write(df)
st.line_chart(df2)
