def add(n1,n2):
    res = n1+n2
    return res

def sub(n1,n2):
    res = n1-n2
    return res

def mul(n1,n2):
    res = n1*n2
    return res

def div(n1,n2):
    res = n1/n2
    return res
#메인
num1, num2 = map(int,input("숫자 2개를 입력하세요 : ").split(' '))
opr = input("연산자 입력 : ")

if opr == '+':
    result = add(num1, num2)
    print("%d %c %d = %.1f" % (num1, opr, num2, result))

elif opr == '-':
    result = sub(num1, num2)
    print("%d %c %d = %.1f" % (num1, opr, num2, result))

elif opr == '*':
    result = mul(num1, num2)
    print("%d %c %d = %.1f" % (num1, opr, num2, result))

elif opr == '/':
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = div(num1, num2)
        print("%d %c %d = %.1f" % (num1, opr, num2, result))
else:
    print("연산자 오류!!")
