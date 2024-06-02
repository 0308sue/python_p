#<
for i in range(1, 10):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(10,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print()

#>
for i in range(1,10):
    for j in range(1,10-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(1,10):
    for k in range(1,i+1):
        print(" ",end=' ')
    for j in range(1,10-i):
        print("*",end=' ')
    print()
