#함수 호출 부분
#점수 3개 입력 map, split으로 구분 리스트에 담기
#모튜 사용 총점 평균 등급 출력
from pyScore import *

L = []
a, b, c = map(int,input("점수 3개 입력 : ").split())

L.append(a)
L.append(b)
L.append(c)

mySum = sum(L)
myAvg = avg(mySum,L)
myGrade = grade(myAvg)

print(f"총점 : {mySum}, 평균 : {myAvg:.1f}, 등급 : {myGrade}")

