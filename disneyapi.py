import streamlit as st
import requests

# DisneyAPIのエンドポイント
API_URL = "https://api.disneyapi.dev/characters"

# タイトルと説明
st.title("Disneyキャラクター検索アプリ")
st.write("DisneyAPIを使用してディズニーキャラクターを検索します。")

# ユーザーからキャラクター名を入力
character_name = st.text_input("キャラクター名を入力してください")

# ボタンが押されたらリクエストを送信
if st.button("検索"):
    # DisneyAPIにリクエストを送信してキャラクター情報を取得
    response = requests.get(API_URL, params={"name": character_name})
    data = response.json()

    # 結果の処理
    if data.get("data"):
        character_info = data["data"][0]  # 最初のキャラクター情報を取得
        st.write(f"**名前**: {character_info['name']}")
        st.write(f"**映画**: {', '.join(character_info.get('films', []))}")
        st.write(f"**ショー**: {', '.join(character_info.get('tvShows', []))}")
        st.write(f"**ビデオゲーム**: {', '.join(character_info.get('videoGames', []))}")
        
        # 画像の表示
        if character_info.get("imageUrl"):
            st.image(character_info["imageUrl"], caption=character_info["name"])
    else:
        st.write("キャラクターが見つかりませんでした。別の名前で試してください。")
