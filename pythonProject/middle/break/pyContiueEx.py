hab = 0

for i in range(1,101):
    if i % 2 : # 0 이외의 모든 숫자는 TRUE
        continue
    hab += i

print("hab = ",hab)

# i = 1
#
# while i < 101:
#     if i % 2 :
#         i += 1
#         continue
#     hab += i
#     i += 1
# print("hab = ", hab)