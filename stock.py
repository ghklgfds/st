import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web

import plotly.express as px

st.title('sp500と日経平均株価の比較')
#st.write(<script src="https://adm.shinobi.jp/s/a4cba23f97bf39157c53a5bfb36b043b"></script>, allow_javascript=True, allow_html=True)

start=dt.date(2011,1,1)
end=dt.date(2021,9,1)
code="SP500"
code2="NIKKEI225"
df=web.DataReader(code,"fred",start,end)
df2=web.DataReader(code2,"fred",start,end)
st.text(df2.columns)
#st.write(df)
st.write(
px.line(df, title="sample figure")
)
st.write (
px.line(df2, title="sample figure")
)

a=df['SP500']
b=df['NIKKEI225']

st.line_chart([a,b])
