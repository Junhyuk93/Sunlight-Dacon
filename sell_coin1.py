from key import Key
from Bit_main import bit_main 
import time
import pybithumb

key = Key()
con_key = key.con_key 
sec_key = key.sec_key
bithumb = bit_main(con_key,sec_key)

# 판매하기 
# 지정가격으로
# order = bithumb.sell_limit_order("EVZ",40.0,20)

# 잔고를 조회해서 비트코인 수량 만큼 지정가 매도 주문 
unit = bithumb.get_balance("EVZ")[0] - bithumb.get_balance("EVZ")[1]
print("현재 남아잇는 코인은:",unit,"개 입니다")
# 전량 넘기기 가능 
order = bithumb.sell_limit_order("EVZ",39.3,unit)
print("판매완료:",order)

# 시장가로 파는건 
# 갯수 조회해서 
# unit = bithumb.get_balance("EVZ")[0] - bithumb.get_balance("EVZ")[1]
# order = bithumb.sell_market_order("EVZ",unit)
# print("판매완료:",order)
