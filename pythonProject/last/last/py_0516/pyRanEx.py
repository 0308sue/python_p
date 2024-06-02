import random as r
print(r.random)
print(r.randrange(1,7))

for i in range(r.randrange(0,3)):
    print(i)

for i in range(10):
    print(r.randrange(0,3),end=' ')

print()

for i in range(10):
    print(r.randrange(1,11,2),end=' ')

for i in range(10):
    print(r.randint(1,10))

L = [10,20,30,40,50]
L = r.shuffle(L)
print(L)
