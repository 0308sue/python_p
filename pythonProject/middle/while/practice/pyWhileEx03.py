# 계속 숫자 입력 받다가 문자 나오면 종료, 짝수 개수 구하기
i = 0
cnt = 1
while True :
    aa = int(input("숫자를 입력하시고 종료하려면 문자를 입력하세요 : "))
    if type(aa) == int :
        if aa % 2 == 0 :
            cnt += 1

    else :
        print('종료')
        print(cnt)
        break
