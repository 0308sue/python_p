while True:
    p1 = input("플레이어 1 : ")
    p2 = input("플레이어 2 : ")

    if p1 == "가위":
        if p2 == "가위":
            print("비겼습니다.")
        elif p2 == "바위":
            print("플레이어 2가 이겼습니다.")
        elif p2 == "보":
            print("플레이어 1이 이겼습니다.")
    elif p1 == "바위":
        if p2 == "가위":
            print("플레이어 1이 이겼습니다.")
        elif p2 == "바위":
            print("비겼습니다.")
        elif p2 == "보":
            print("플레이어 2가 이겼습니다.")
    elif p1 == "보":
        if p2 == "가위":
            print("플레이어 2가 이겼습니다.")
        elif p2 == "바위":
            print("플레이어 1이 이겼습니다.")
        elif p2 == "보":
            print("비겼습니다.")
    else:
        print("입력 오류!")
        break

    retry = input("계속하시겠습니까? ")
    if retry =='y':
        continue
    else :
        break
print("프로그램 종료")

