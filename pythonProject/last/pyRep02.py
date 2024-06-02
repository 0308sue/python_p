def myDan(n):#한 단을 출력
    print(f"# {n}단 #")
    for i in range (1,10):
        print(f"{n} x {i} = {n*i}")
def myAllDan(): #구구단 전체
    i = 1
    while i < 10 :
        print(f"# {i}단 #")
        j = 1
        while j < 10:
            print("%d x %d = %d" %(i,j,i*j))
            j+=1
        print()
        i+=1

# main
while True:
    num = int(input("숫자를 입력하세요(1 - 한단, 2 - 전체, 0 - 종료)  : "))

    if num == 1 :
        dan = int(input("단을 입력하세요 : "))
        myDan(dan)

    elif num == 2 :
        myAllDan()

    elif num == 0 :
        break

    if input("계속 하시겠습니까?(y/n) : ") == 'n' :
        break

print('프로그램 종료!')