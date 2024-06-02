# 랜덤 함수 써서 가위바위보 짜기 0전 0승 0패 까지 출력
import random as r

game, win, lose, draw = 0,0,0,0
srp = ['가위','바위','보']

while True:
    my_srp = srp.index(input("가위? 바위? 보? : "))
    com_srp = r.randint(0,2)
    game += 1
    print(f"나 : {srp[my_srp]}, 컴퓨터 : {srp[com_srp]}")
    if my_srp == com_srp :
        print('비김')
        draw += 1

    elif my_srp + 1 == com_srp or my_srp - 2 == com_srp :
        print("짐")
        lose += 1

    else:
        print("이김")
        win += 1

    if input('종료 ? ㅇ/ㄴ : ') == 'ㅇ':
        break

print("{0}전 {1}승 {2}무 {3}패".format(game,win,draw,lose))