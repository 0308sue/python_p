# 동전 교환 프로그램

price = int(input("교환할 금액을 입력하세요 : "))
left = 0

if price > 500 :
    print(f"500원 : {price // 500}개")
    price = price % 500

if price > 100 :
    print(f"100원 : {price // 100}개")
    price %= 100

if price > 50 :
    print(f"50원 : {price // 50}개")
    price %= 50

if price > 10 :
    print(f"10원 : {price // 10}개")
    price %= 10


print(f"남은 돈은 {price}원 입니다.")