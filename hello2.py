import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web

import plotly.express as px

st.title('Streamlit sp500')

start=dt.date(2021,1,1)
end=dt.date(2021,3,1)
code="SP500"
df=web.DataReader(code,"fred",start,end)
st.text(df.columns)
st.write(df.head(100))
st.write(
    px.line(x=["SP500"], y=[1,3,2], title="sample figure")
)
