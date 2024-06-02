L = [] #빈 리스트
L2 = []
hab = 0
num = 0

for i in range(0,5):
    # print(L[i])
    # L.append((i+1))
    num = 0
    num = int(input("%d 번째 숫자 : "%(i+1)))
    if num%2 == 0 :
        L.append(num)
        hab += num
    else:
        L2.append(num)

for i in range(0,len(L)):
    # print(L[i])
    print("L[%d]=%d"%(i+1,L[i]))
for i in range(0, len(L2)):
    # print(L[i])
    print("L2[%d]=%d"%(i+1,L2[i]))
print(hab)
print(hab/len(L))