#리스트에 1~8까지 저장
#리스트에서 맵 함수로 뽑고 람다 함수로 제곱 한튀에 리스트로 저장 후 출력

a = list(range(1,8))

L = list(map(lambda x : x**2,a))

print(L)