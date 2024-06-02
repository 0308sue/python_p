num1 =int(input("첫번째 숫자 : "))
num2 =int(input("두번째 숫자 : "))
opr = input("연산자 :")

if opr =='+':
    res = num1 + num2
    print("%d %c %d = %d"%(num1, opr, num2,res))

elif opr == '-':
    res = num1 - num2
    print("%d %c %d = %d" % (num1, opr, num2, res))

elif opr == '*':
    res = num1 * num2
    print("%d %c %d = %d" % (num1, opr, num2, res))

elif opr == '/':
    if num2 != 0 :
        res = num1 / num2
        print("%d %c %d = %.1f" % (num1, opr, num2, res))
    else :
        print("0으로 나눌 수 없습니다.")

else:
    print("연산자 오류!!")