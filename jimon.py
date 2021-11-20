import pandas as pd

while True:
    nayami = input("あなたが尊敬する人がいるとして、その人はなんて言ってますか？")
    bnayami=input(nayami+"についてどうすべきですか？")
    print(nayami,bnayami)
    data=[nayami,bnayami]
    df=pd.DataFrame(data)
    df.T.to_csv("nayami.csv",mode="a",index=False,header=False)
    d=input("続けるならｙを入力してください")
    if d!="ｙ":
        break
    else:
        nayami=bnayami
