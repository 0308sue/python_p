#map, split을 이용해 정수 2개 입력 받아서 ',' 기준으로 반가리
num1 = 10
num2 = 20

num1,num2= map(int,input('정수 2개를 입력하세요 : ').split(' '))
print(num1)
print(num2)