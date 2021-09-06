import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web

import plotly.express as px

st.title('sp500と日経平均株価の比較')

start=dt.date(2011,1,1)
end=dt.date(2021,9,1)
code="SP500"
code2="NIKKEI225"
df=web.DataReader(code,"fred",start,end)
df2=web.DataReader(code2,"fred",start,end)
st.text(df.columns)
#st.write(df)
st.write(
px.line(df,df2, title="sample figure")
)
