# 수 5개 입력 받아서 최대값 최소값 판별 max, min을 첫번째 입력받은 num으로 설정
# for while 둘다

num1 = int(input("1번째 숫자를 입력하세요 : "))
min = max = num1

# for i in range(2,6):
#     num = int(input(f"{i}번째 숫자를 입력하세요 : "))
#     if num < min :
#         min = num
#     if num > max :
#         max = num

i = 2

while i < 6:
    num = int(input(f"{i}번째 숫자를 입력하세요 : "))
    if num < min :
        min = num
    if num > max :
        max = num
    i += 1

print(f"최댓값 : {max}, 최솟값 : {min}")



