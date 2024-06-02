L = ['','','','',''] #빈 리스트
hab = 0

for i in range(0,5):
    # print(L[i])
    # L.append((i+1))
    L[i] = int(input("%d 번째 숫자 : "%(i+1)))
    hab += L[i]

for i in range(0,5):
    # print(L[i])
    print("L[%d]=%d"%(i,L[i]))
print(hab)
print(hab/len(L))