import urllib.request as req
import json
import streamlit as st

St.title("The weather in Japan")
# URLや保存ファイル名を指定
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
# ダウンロード
req.urlretrieve(url, filename)

# ダウンロードしたファイルを開く --- (*1)
with open('tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)
# 読み出したデータを解析 --- (*2)
for area in data:
  name = area['name']
  st.text(name)
  for ts in area['srf']['timeSeries']:
    times = [n for n in ts['timeDefines']]
    if 'weathers' in ts['areas']:
      for i,v in enumerate(ts['areas']['weathers']):
        st.text(times[i])
        st.text(v)
        

