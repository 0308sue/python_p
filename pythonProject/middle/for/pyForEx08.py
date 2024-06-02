a = 1
N = int(input('N을 입력 => '))
print(f'{N}!은')
for b in range(1, N+1, 1):
    if N%b == 0 :
        if b == N :
            print("{0}".format(b))
        else :
            print(f'{b}', end=' * ')
