from key import Key
from Bit_main import bit_main 
import time
import pybithumb

key = Key()
con_key = key.con_key 
sec_key = key.sec_key
bithumb = bit_main(con_key,sec_key)

# 원화 잔고
krw = bithumb.get_balance("EVZ")[2]

# 현제 비트코인 시세 확인
# 최우선 매도 호가 금액 찾기 
orderbook = pybithumb.get_orderbook("EVZ")
asks = orderbook["asks"]
sell_price = asks[0]['price']
print("구매가격:",sell_price)

# 내 잔고에서 25% 만 나눠서 비트 코인 구매 (분산 투자)
buy_money = krw/4
unit = buy_money/(sell_price)
print("구매 갯수:",unit)

# 주문
order = bithumb.buy_market_order("EVZ",unit)
print("주문성공?",order)