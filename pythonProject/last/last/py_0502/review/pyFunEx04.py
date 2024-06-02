# 함수 사용, 숫자를 입력했을 때 1부터 그 숫자까지 소수 개수
def even(n):
    L1 = []
    for i in range(1,n+1):
        if i % 2 == 0:
            L1.append(i)
    print("짝수 : ",L1)
    print("짝수의 개수 : ",len(L1))


#main
num = int(input("숫자 입력 : "))
even(num) #함수 호출
