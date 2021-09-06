import urllib.request as req
import json

import streamlit as st


# URLや保存ファイル名を指定
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
# ダウンロード
req.urlretrieve(url, filename)

# ダウンロードしたファイルを開く --- (*1)
with open('tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)
# 読み出したデータを解析 --- (*2)
tank=[]
tank2=[]
for area in data:
  name = area['name']
  

  print("[", name, "]")
  for ts in area['srf']['timeSeries']:
    times = [n for n in ts['timeDefines']]
    if 'weathers' in ts['areas']:
      for i,v in enumerate(ts['areas']['weathers']):
        print(times[i], ":", v)
        #
        b=[times[i], ":", v]
        #
        
        #c2=str[c[1]].replace["u3000",""]
        tank.append(b)
      tank2.append(name,tank)
      tank=[]
        
print(tank2)
st.title(tank2)
