max, min = 0,10 #변수 초기화

for i in range(1,6):
    num = int(input("%d번째 숫자 : "%i))
    if max < num:
        max = num

    if min > num:
        min = num

print("최댓값 : %d"%max)
print("최솟값 : %d"%min)
