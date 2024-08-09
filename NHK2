import requests
import pandas as pd
import streamlit as st
import datetime

def display_program_info(tank, titles):
    st.write('番組情報')
    select_title = st.sidebar.radio('タイトル', titles)
    
    for t in tank:
        if t[2] == select_title:
            st.write('開始時間:', t[0])
            st.write('終了時間:', t[1])
            st.write('タイトル:', t[2])
            st.write('サブタイトル:', t[3] or 'なし')
            st.write('概要:', t[4] or 'なし')
            st.write('出演者:', t[5] or 'なし')
            break

def display_actor_info(tank, acttank):
    select_act = st.sidebar.radio('出演者', acttank)
    
    for v in tank:
        if select_act and v[5] == select_act:
            st.write('開始時間:', v[0])
            st.write('終了時間:', v[1])
            st.write('タイトル:', v[2])
            st.write('サブタイトル:', v[3] or 'なし')
            st.write('概要:', v[4] or 'なし')
            st.write('出演者:', v[5] or 'なし')
            break

def fetch_program_data(channel, day, month, key):
    url = f'https://api.nhk.or.jp/v2/pg/list/130/{channel}/2023-{month}-{day}.json?key={key}'
    response = requests.get(url)
    
    if len(response.text) == 51:
        st.text('番組情報がまだありません。')
        return []
    else:
        return response.json()['list'][channel]

def parse_program_data(program_data):
    tank = []
    for i in program_data:
        starttime = i['start_time'][11:16]
        endtime = i['end_time'][11:16]
        title = i['title']
        subtitle = i.get('subtitle', 'なし')
        content = i.get('content', 'なし')
        act = i.get('act', 'なし')
        tank.append([starttime, endtime, title, subtitle, content, act])
    
    return tank

def main():
    st.title('NHKの番組を探す')

    f = open('Key.txt', 'r', encoding='UTF-8')
    key = f.read().strip()
    f.close()

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    day = st.slider("日付", 1, 31, now.day)
    month = str(now.month).zfill(2)

    channel_map = {
        '総合': 'g1', 'Eテレ': 'e1', 'BS1': 's1', 
        'BSプレミアム': 's3', 'ＮＨＫラジオ第1': 'r1',
        'ＮＨＫラジオ第2': 'r2', 'ＮＨＫＦＭ': 'r3'
    }
    
    selectchannel = st.radio('', list(channel_map.keys()))
    channel = channel_map[selectchannel]

    program_data = fetch_program_data(channel, day, month, key)
    if program_data:
        tank = parse_program_data(program_data)
        df = pd.DataFrame(tank)
        titles = df[2].tolist()
        acts = df[5].tolist()
        acttank = [act for act in acts if act]

        selectmethod = st.radio('', ('タイトルで探す', '出演者で探す'))
        if selectmethod == 'タイトルで探す' and tank:
            display_program_info(tank, titles)
        elif selectmethod == '出演者で探す' and tank:
            display_actor_info(tank, acttank)

if __name__ == "__main__":
    main()
