# 1 ~ 100 소수만 한줄에 출력 while 사용, cnt 대입 연산자 사용
cnt = 0

# for num in range(2,101):
#     for i in range(1,num+1):
#         if num % i == 0 :
#             cnt += 1
#
#     if cnt == 2 :
#         print(num, end=' ')
#     cnt = 0
num = 2
hap = 0
while num <= 100:
    i = 1
    while i <= num:
        if num % i == 0 :
            cnt += 1
        i += 1
    if cnt == 2:
        print(num, end = ' ')
        hap += 1
    cnt = 0
    num += 1
print(hap,'개')

