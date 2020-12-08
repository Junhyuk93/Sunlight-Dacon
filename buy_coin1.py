from key import Key
from Bit_main import bit_main 
import time
import pybithumb

key = Key()
con_key = key.con_key 
sec_key = key.sec_key
bithumb = bit_main(con_key,sec_key)

# 시장가로 구매

order = bithumb.buy_market_order("EVZ",30)
# 최소 금액 때문에 30개 단위로 구매 해야함
# 최소 금액 1000원
# evz 한개 가격 37원
print(order)