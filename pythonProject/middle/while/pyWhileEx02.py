# dan = int(input("단을 입력하세요 : "))
i = 2

while i < 10:
    j = 1
    while j <10:
        res =i * j
        print("%d x %d = %d" % (i, j, res))
        j += 1
        # print(i,'x',dan,'=',res)
    print()
    i += 1
