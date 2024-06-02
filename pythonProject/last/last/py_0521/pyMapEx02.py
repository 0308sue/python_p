def square(n):
    return n**2

a = list(range(1,8))
L = list(map(square,a))

print(L)