num=int(input("숫자를 입력하세요 : "))
for i in range(2,num+1):
    if num%i==0:
        if num!=i:
            print(num,"은(는) 소수가 아닙니다")
            break
        else:
            print(num, "은(는) 소수 입니다")



