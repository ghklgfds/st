import pandas as pd
import streamlit as st

while True:
    #nayami = input("あなたが尊敬する人がいるとして、その人はなんて言ってますか？")
    nayami=st.text_input('First name')
    bnayami=st.text_input(nayami+"についてどうすべきですか？")
    st.write(nayami)
    st.write(bnayami)
    d=st.text_input("続けるならｙを入力してください")
    if d!="ｙ":
        break
    else:
        nayami=bnayami
