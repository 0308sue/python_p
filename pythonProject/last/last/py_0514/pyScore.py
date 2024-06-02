#모튤 부분
#총점, 평균, 등급 출력
#__name__


def syn(L):
    res = 0
    for i in range(len(L)):
        res += L[i]
    return res

def avg(total,L):
    res = total/len(L)
    return res

def grade(a):
    if a >= 90 :
        res = 'A'
    elif a >= 80 :
        res = 'B'
    elif a >= 70 :
        res = 'C'
    elif a >= 60 :
        res = 'D'
    return res

if __name__ == '__main__':
    L = [90, 90, 90]
    hab = sum(L)
    myAvg = avg(hab,L)
    myGrade = grade(myAvg)
    print(hab)
    print(myAvg)
    print(myGrade)
