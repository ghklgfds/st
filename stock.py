import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web
import plotly.express as px

today = dt.date.today()

year = today.year
month = today.month
day = today.day

print(year)  
print(month)  
print(day)  


st.title('sp500と日経平均株価の比較')
start=dt.date(2018,1,1)
end=dt.date(year,month,day)
code="SP500"
code2="NIKKEI225"
df=web.DataReader(code,"fred",start,end)
df2=web.DataReader(code2,"fred",start,end)
#st.text(df2.columns)
#st.write(df)
st.write(
px.line(df, title="SP500")
)
st.write (
px.line(df2, title="日経平均株価")
)

a=df['SP500']
b=df2['NIKKEI225']
tank=[]
for (x,y) in zip (a,b):
    z=(10*x,y)
    tank.append(z)
[m,n]=tank[-1]

#st.text ("SP500は10倍で描画")
#st.text(str(m/10)+"ドル"+str(n)+"円")
df3=pd.DataFrame(tank)

st.line_chart(df3)
