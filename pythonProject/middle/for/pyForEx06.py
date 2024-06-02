# for i in range(10):
#     print("{0} : Hello python!".format(i))
#
# for i in [0,1,2] :
#     print(i)
#
# for i in "Python" :
#     print(i,end=" ")
#

num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

sum = 0
for i in range(num1,num2+1,1):
    sum += i
print(f"{num1}~{num2}까지의 합은 {sum}")