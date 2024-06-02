nList = [-30,45,-5,-90,20,53,77,-36]
minusList = list(filter(lambda x:x<0,nList))

print(minusList)

print('='*50)

import random as rd

nList = []
for i in range (1,11):
    rnd = rd.randint(1,10)
    nList.append(rnd)

evenList = list(filter(lambda x:x%2==0,nList))

print(nList)
print(evenList)