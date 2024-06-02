L = ['','','','',''] #빈 리스트

for i in range(0,5):
    # print(L[i])
    # L.append((i+1))
    L[i] = int(input("%d 번째 숫자 : "%(i+1)))

for i in range(0,5):
    # print(L[i])
    print("L[%d]=%d"%(i,L[i]))
# print(L[0])
# print(L[1])
# print(L[2])
# print(L[3])
# print(L[4])