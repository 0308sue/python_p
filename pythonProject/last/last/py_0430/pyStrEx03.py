s = input('문자열 입력 : ')

if s.startswith('(') == False :
    s = '('+s
if s.endswith(')') == False :
    s = s+')'

print( s )