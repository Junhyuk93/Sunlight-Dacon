from key import Key
from Bit_main import bit_main 

# 키를 확인하는 함수 
key = Key()
con_key = key.con_key 
sec_key = key.sec_key

# 발란스 확인하는 함수 
from Bit_main import bit_main 
bithumb = bit_main(con_key,sec_key)
print("보유중(EVZ) :",bithumb.get_balance("EVZ")[0],"개","거래중(매도중) :",bithumb.get_balance("EVZ")[1],"개",\
    "보유중(원화) :",bithumb.get_balance("EVZ")[2],"원","주문에 사용된(원화) :",bithumb.get_balance("EVZ")[3],"원")


