# 소수 판별

num = int(input("숫자를 입력해 주세요 : "))

i = 2
while i < num+1 :
    if num % i == 0 and i != num:
        print(num,"은(는) 소수가 아닙니다.")
        break
    if num % i == 0 and i == num:
        print(num,"은(는) 소수입니다.")
        break
    i += 1