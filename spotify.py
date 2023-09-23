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

#から邦楽のトラックを取得する処理を追加する

st.write("楽曲情報をspotifyから取得する")
s.write("指定したアーティストの楽曲データを取得できます。その曲のテンポ、キー、曲調もデータとして取得できます。")



artist_name=st.text_input("アーティスト名を入力してください。")




# 検索するアーティスト名を指定
#artist_name = 'Michael Jackson'

# アーティストを検索
results = sp.search(q='artist:' + artist_name, type='artist')

# アーティストIDを取得
artist_id = results['artists']['items'][0]['id']
#artist_id="5FLbE1s9bnHwJhmngtVXpD"
print (artist_id)
all_tracks = sp.artist_albums(artist_id=artist_id, album_type='album', country='JP', limit=3)
print (all_tracks)
# トラックのIDをリストに格納
track_ids = []
for album in all_tracks['items']:
    album_tracks = sp.album_tracks(album['id'])
    for track in album_tracks['items']:
        track_ids.append(track['id'])

# トラックを複数のグループに分けてAPIリクエストを行い、audio featuresを取得
audio_features = []
for i in range(0, len(track_ids), 100):
    audio_features.extend(sp.audio_features(track_ids[i:i+100]))

# データフレームにまとめる
df = pd.DataFrame(audio_features)

df['name'] = [sp.track(track_id)['name'] for track_id in track_ids]
df['popularity'] = [sp.track(track_id)['popularity'] for track_id in track_ids]
df['release_date'] = [sp.track(track_id)['album']['release_date'] for track_id in track_ids]

# 不要な列を削除
#df.drop(['type', 'id', 'uri', 'track_href', 'analysis_url'], axis=1, inplace=True)
# 列の順番を調整
df = df[['name', 'popularity', 'release_date', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
if df==[]:
    st.write("入力したデータが誤っているか、存在しません。邦楽アーティストの場合はローマ字だと出力できる場合があります。")
    
# データフレームを表示
st.dataframe(df)
