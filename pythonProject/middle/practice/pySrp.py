import random as r
srp = ['가위', '바위', '보']

# for i in range(5):
#     rnd = r.randint(0, 2)
#     print(srp[rnd], end=' ')
#
challenge,win,draw,lose = 0,0,0,0

while True:
    challenge += 1
    csrp = r.randint(0,2)
    mysrp = input("가위? 바위? 보? : ")
    if mysrp == '가위':
        isrp =0
    elif mysrp == '바위':
        isrp =1
    elif mysrp == '보':
        isrp =2
    else :
        input("잘못 입력하였습니다.")
        break

    if isrp == csrp:
        print(f"나 : {mysrp}, 컴퓨터 : {srp[csrp]}")
        print("비겼습니다.\n")
        draw += 1
    elif isrp == (csrp - 2) or isrp == (csrp+1):
        print(f"나 : {mysrp}, 컴퓨터 : {srp[csrp]}")
        print("이겼습니다.\n")
        win += 1
    else:
        print(f"나 : {mysrp}, 컴퓨터 : {srp[csrp]}")
        print("졌습니다.\n")
        lose += 1

    retry = input("계속 하시겠습니까? (y/n)")
    if retry != "y":
        break
    else:
        continue

print(f"{challenge}전/ {win}승/ {draw}무/ {lose}패")
print("프로그램 종료!")
