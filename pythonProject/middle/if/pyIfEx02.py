# a = int(input("첫번째 숫자 : "))
# b = int(input("두번째 숫자 : "))
# c = int(input("세번째 숫자 : "))

a, b, c = map(int,input("숫자 3개를 입력하세요 : ").split(','))

if a>b :
    if a>c :
        max = a
    else :
        max = b
else:
    if b>c :
        max = b
    else :
        max = c
print(f"가장 큰수는 {max}입니다.")


