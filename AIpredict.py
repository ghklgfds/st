import streamlit as st
from prophet import Prophet
import yfinance as yf
import pandas as pd

def yosou(symbol, predicttime):
    # データの取得
    data = yf.download(symbol, period="7d", interval="1m", progress=False)
    data = data.reset_index()

    # タイムゾーンの除去と列名の確認
    if 'Datetime' in data.columns:
        data['ds'] = data['Datetime'].dt.tz_localize(None)
    elif 'Date' in data.columns:
        data['ds'] = data['Date'].dt.tz_localize(None)
    else:
        st.error("Datetime列が見つかりません")
        return None  # エラー時にNoneを返す

    # データの正規化
    data['y'] = data['Close'] / data['Close'].max()  # 予測対象の列の追加

    # モデルの定義
    model = Prophet()

    # モデルの学習
    model.fit(data[['ds', 'y']])

    # 予測用のデータフレームを作成
    future = model.make_future_dataframe(periods=predicttime, freq='T')

    # 予測
    forecast = model.predict(future)

    # 元のデータの最大値を取得
    original_max = data['Close'].max()

    # 'yhat'列の最後の値を元の最大値で乗算して1時間後の予測価格を求める
    predicted_price = forecast['yhat'].iloc[-1] * original_max

    return predicted_price

def main():
    predicttime = 60
    symbols = ["BTC-USD"]
    
    if st.button("ビットコインの1時間後の予測を実行"):
        for symbol in symbols:
            result = yosou(symbol, predicttime)
            if result is not None:
                st.write(f"{symbol}の1時間後の予測価格は: {result} USD")
            else:
                st.write(f"{symbol}の予測に失敗しました。")

if __name__ == "__main__":
    main()
