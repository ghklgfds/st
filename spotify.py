import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

# Spotify APIのクライアントIDとクライアントシークレットを指定
client_id = 'e039088e0ef7444faf5ec7e5a7f01ee1'
client_secret = '5be9bc0f583d4d75981e3b0686b4a226'

# Spotify APIにアクセスするための認証を取得
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

st.title("Spotify アーティストの楽曲情報取得")

# ユーザーにアーティスト名を入力してもらう
artist_name = st.text_input("アーティスト名を入力してください:")

if artist_name:
    try:
        # アーティストを検索
        results = sp.search(q='artist:' + artist_name, type='artist')
        
        if results['artists']['items']:
            # アーティストIDを取得
            artist_id = results['artists']['items'][0]['id']
            st.write(f"アーティストID: {artist_id}")

            # アルバム情報を取得
            all_albums = sp.artist_albums(artist_id=artist_id, album_type='album', country='JP', limit=20)
            
            if all_albums['items']:
                # アルバム情報をデータフレームに格納
                albums_data = []
                for album in all_albums['items']:
                    albums_data.append({
                        'アルバム名': album['name'],
                        'リリース日': album['release_date'],
                        '総トラック数': album['total_tracks']
                    })
                
                df = pd.DataFrame(albums_data)
                st.dataframe(df)
            else:
                st.write("指定したアーティストのアルバム情報が見つかりませんでした。")
        else:
            st.write("アーティストが見つかりませんでした。正しい名前を入力してください。")

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
else:
    st.write("アーティスト名を入力してください。")
