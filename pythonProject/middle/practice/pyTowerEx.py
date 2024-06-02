# for i in range(1,10):
#     for j in range(1,10):
#         print("#",end=' ')
#     print()'

i = 1
while i <= 10:
    j = 1
    while j <= i:
        print("#",end=' ')
        j += 1
    i += 1
    print()

i = 1
while i <= 10:
    j = 1
    while j <= 11-i:
        print("#", end=' ')
        j += 1
    i += 1
    print()

