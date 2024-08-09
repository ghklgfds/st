import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler

def yosou(symbol, predicttime):
    # データの取得
    data = yf.download(symbol, period="7d", interval="1m", progress=False)
    data = data.reset_index()

    # タイムゾーンの除去と列名の確認
    if 'Datetime' in data.columns:
        data['ds'] = data['Datetime'].dt.tz_localize(None)
    elif 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # 日時型に変換
        data['ds'] = data['Date'].dt.tz_localize(None)
    else:
        st.error("Datetime列またはDate列が見つかりません")
        return None  # エラー時にNoneを返す

    # データの正規化
    scaler = MinMaxScaler()
    data['y'] = scaler.fit_transform(data[['Close']])  # Close列のスケーリング

    # 欠損値の確認と処理
    if data['y'].isnull().sum() > 0:
        st.warning("予測対象のデータに欠損値があります。欠損値は削除されます。")
        data = data.dropna(subset=['y'])

    # 特徴量とターゲットの定義
    X = data.index.values.reshape(-1, 1)
    y = data['y'].values

    # SVRモデルの定義
    model = SVR(kernel='rbf')

    # モデルの学習
    model.fit(X, y)

    # 予測用のデータフレームを作成
    future_index = pd.RangeIndex(start=len(data), stop=len(data) + predicttime, step=1).values.reshape(-1, 1)

    # 予測
    forecast = model.predict(future_index)

    # 予測結果を元のスケールに戻す
    predicted_price = scaler.inverse_transform(forecast.reshape(-1, 1))

    return predicted_price[-1][0]  # 最後の予測価格を返す

def main():
    predicttime = 60
    symbols = ["BTC-USD"]
    
    if st.button("ビットコインの1時間後の予測を実行"):
        for symbol in symbols:
            result = yosou(symbol, predicttime)
            if result is not None:
                st.write(f"{symbol}の1時間後の予測価格は: {result:.2f} USD")
            else:
                st.write(f"{symbol}の予測に失敗しました。")

if __name__ == "__main__":
    main()
