import streamlit as st
from prophet import Prophet
import yfinance as yf
import pandas as pd


def yosou(symbol,predicttime):
  # データの取得
  data = yf.download(symbol, period="7d", interval="1m")
  data = data.reset_index()

  # タイムゾーンの除去
  data['Datetime'] = data['Datetime'].dt.tz_localize(None)  # タイムゾーンを除去

# データの正規化
  data['ds'] = data['Datetime']  # Prophetが要求する日付列の追加
  data['y'] = data['Close'] / data['Close'].max()  # 予測対象の列の追加

# モデルの定義
  model = Prophet()

# データの分割
  train_data = data.iloc[:-1]
  test_data = data.iloc[-1:]

# モデルの学習
  model.fit(train_data[['ds', 'y']])

# 予測用のデータフレームを作成
  future = model.make_future_dataframe(periods=predicttime, freq='T')  # 1時間後の予測を60分後に設定

# 予測
  forecast = model.predict(future)

# 元のデータの最大値を取得
  original_max = data['Close'].max()

# 'yhat'列の最後の値を元の最大値で乗算して1時間後の予測価格を求める
  predicted_price = forecast['yhat'].iloc[-1] * original_max

# 予測結果の出力
  price=(predicted_price)
  st.text(price)
def main():
    predicttime = 60
    symbols = ["BTC-USD"]
    
    if st.button("ビットコインの1時間後の予測を実行"):
        tank2 = []
        for i in symbols:
            result = yosou(i, predicttime)
            tank2.append(result)

if __name__ == "__main__":
    main()
