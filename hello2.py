import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web

start=dt.date(2021,1,1)
end=dt.date(2021,3,1)
code="SP500"
df=web.DataReader(code,"fred",start,end)
st.text(df.head(5))
