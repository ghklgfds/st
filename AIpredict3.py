import streamlit as st
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# データの取得
def get_data():
    df = yf.download('USDJPY=X', interval='1h', period='60d')  # 過去60日間の1時間足データを取得
    return df[['Close']]  # Close価格のみ使用

# データの前処理
def preprocess_data(df):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)

    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i-60:i, 0])
        y.append(scaled_data[i, 0])
    
    X = np.array(X)
    y = np.array(y)

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    return X, y, scaler

# LSTMモデルの構築
def create_model():
    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(60, 1)))
    model.add(Dropout(0.2))

    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(units=25))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    return model

# モデルの訓練
def train_model(X_train, y_train):
    model = create_model()
    model.fit(X_train, y_train, batch_size=1, epochs=1)
    return model

# 予測の実装
def predict_next_hour(model, recent_data, scaler):
    recent_data_scaled = scaler.transform(recent_data)
    X_test = []
    X_test.append(recent_data_scaled)
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    predicted_price = model.predict(X_test)
    predicted_price = scaler.inverse_transform(predicted_price)
    
    return predicted_price[0, 0]

# Streamlitアプリの作成
def main():
    st.title('ドル円予測AI')

    # データ取得と表示
    df = get_data()
    st.line_chart(df['Close'])

    # データの前処理とモデルの訓練
    X_train, y_train, scaler = preprocess_data(df)
    model = train_model(X_train, y_train)

    # 予測の実行
    recent_data = df[-60:].values.reshape(-1, 1)
    predicted_price = predict_next_hour(model, recent_data, scaler)

    # 予測結果の表示
    st.write(f"1時間後のドル円予測価格: {predicted_price:.2f} JPY")

if __name__ == '__main__':
    main()
