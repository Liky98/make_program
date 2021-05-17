import pyupbit

access = "hdrILWr2DzeQqfQwGNRGzd7YlR9szdvI2HAcqxw3"          # 본인 값으로 변경
secret = "SJg4TSKzg68txqNKr2q6A2ByY2QJV09yJZh3eZ16"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

