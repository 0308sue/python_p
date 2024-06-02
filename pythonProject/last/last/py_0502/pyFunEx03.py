def hab():
    n = int(input("숫자를 입력하세요 : "))
    mySum = 0
    for i in range(1,n+1):
        mySum += i
    print(f"1 ~ {n}까지의 합 : {mySum}")

#main
hab()

