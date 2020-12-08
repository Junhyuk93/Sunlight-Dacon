from key import Key
from Bit_main import bit_main 
import time
import pybithumb

# 키를 확인하는 함수 
key = Key()
con_key = key.con_key 
sec_key = key.sec_key

# bithumb api 호출
bithumb = bit_main(con_key,sec_key)

for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)