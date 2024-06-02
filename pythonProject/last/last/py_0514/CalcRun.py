# import pyCalc as calc
from pyCalc import *

n1, n2 = map(int,input('숫자 2개 입력 : ').split())
op = input('연산자 입력 : ')

if op == '+':
    res = add(n1,n2)
    print(f'{n1} {op} {n2} = {res}')

if op == '-':
    res = sub(n1,n2)
    print(f'{n1} {op} {n2} = {res}')

if op == '*':
    res = mul(n1,n2)
    print(f'{n1} {op} {n2} = {res}')

if op == '/':
    res = div(n1,n2)
    print(f'{n1} {op} {n2} = {res:.1f}')
