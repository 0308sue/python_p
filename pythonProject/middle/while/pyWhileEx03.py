cnt = 0
i = 1
while True :
    num = int(input("%d숫자 : "%i))
    if num < 0:
        break;
    if num%2 == 0:
        cnt +=1
    i += 1
print("짝수의 개수 : ",cnt)