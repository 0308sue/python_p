# *로 > 모양 출력
for i in range(1,11):
    if i > 5 :
        for j in range(10-i,1,-1):
            print('*', end='')
    else :
        for j in range(1,i+1):
            print('*', end='')

    print()