hab = 0
# for i in range(1,101):
#     hab += i
#
#     if hab>=100:
#         break
# print("합이 1000이 넘는 최초의 수 : ",i)
# print("hab =",hab)

i = 1


while i < 101 :
    hab += i
    if hab > 100:
        break
    i += 1

print("합이 1000이 넘는 최초의 수 : ",i)
print("hab =",hab)