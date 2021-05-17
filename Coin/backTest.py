import pyupbit
import numpy as np

#ohlcv > open당일시가, high고가, low저가, close종가, volume거래량
df = pyupbit.get_ohlcv("KRW-BTC", count=10) #10일동안의 데이터

#변동성 돌파 기준범위 계산, (고가-저가) * 0.5(k)
df['range'] = (df['high'] - df['low']) * 0.5

#target매수가, range 컬럼을 한칸씩 밑으로 내림
df['target'] = df['open'] + df['range'].shift(1)

#fee = 0.0032 (수수료)

#ror수익율 where(조건문, 참, 거짓)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] ,
                     1)

#누적 곱 계산(cumprod) > 누적수익률
df['hpr'] = df['ror'].cumprod()

#draw Down계산(누적 최대값과 현제 hpr차이 / 누적최대값*100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 계산
print("MDD(%): ", df['dd'].max())

#엑셀로 저장 및 출력
df.to_excel("dd.xlsx")
