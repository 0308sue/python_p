num = int(input("숫자를 입력하세요 : "))
cnt,hab = 0,0

for i in range(1, num+1, 1):
    if num %i==0:
        print(i,end=' ')
        cnt += 1
        hab += i
print("")
print(f"{num}의 약수 개수 : {cnt}")
print(f"{num}의 약수 합 : {hab}")

