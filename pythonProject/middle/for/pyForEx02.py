num = int(input("숫자를 입력하세요 : "))
cnt = 0

for i in range(1,num+1):
    if num%i == 0 :
        cnt += 1
if cnt == 2:
    print(f"{num}은 소수입니다.")
else :
    print(f"{num}은 소수가 아닙니다.")
