s = ('Python is Easy.')
print(s)
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())

s = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠.^^'

print(s.count('공부'))

print(s.find('공부'))

#찾는건 오른쪽에서 부터 카운트는 왼쪽에서 부터
print(s.rfind('공부'))