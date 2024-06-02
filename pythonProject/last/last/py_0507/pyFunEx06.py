#로또 출력
#랜덤 함수 사용 1~50
#while True 사용
#6개씩 5줄 나오도록
import random

def getNumber():
    return random.randrange(1, 46)

Lotto = []

for i in range(5):
    Lotto.clear()
    while True:
        num = getNumber()
        if Lotto.count(num) == 0:
            Lotto.append(num)

        if len(Lotto) >= 6:
            break
    Lotto.sort()
    print(Lotto)