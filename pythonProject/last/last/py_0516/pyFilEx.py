# ages = [34,30,20,18,13,54]
#
# def adult_func(n):
#     if n >19 :
#         return True
#     else :
#         return False
#
# print('성년 리스트 : ')
# for a in filter(adult_func, ages):
#     print(a,end=' ')

#람다 함수로
ages = [34,30,20,18,13,54]

print('성년 리스트 : ')
for a in filter(lambda x : x >=19, ages):
    print(a,end=' ')

print()

#람다 함수로 고급 Ver.
ages = [34,30,20,18,13,54]

print('성년 리스트 : ')
adult = list(filter(lambda x : x >=19, ages))
print(adult,end=' ')


