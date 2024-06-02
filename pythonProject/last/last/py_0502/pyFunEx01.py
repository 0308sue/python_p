def calc(n1, n2, op):
    if op == '+':
        res = n1 + n2

    elif op == '-' :
        res = n1 - n2

    elif op == '*' :
        res = n1 * n2

    elif op == '/':
        res = n1/n2

    return res

num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))
opr = input("연산자 : ")
result = calc(num1, num2, opr)
print("%d %c %d = %.1f"%(num1, opr, num2, result))
