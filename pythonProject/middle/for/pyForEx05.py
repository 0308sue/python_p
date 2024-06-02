num = int(input("1번째 숫자 : "))
max = min = num

for i in range(2, 6):
    num = int(input("%d번째 숫자 : "%i))
    if max<num:
        max = num

    if min>num:
        min = num

print("최댓값 :",max)
print("최솟값 :",min)
