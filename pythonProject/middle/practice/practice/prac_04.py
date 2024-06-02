# 구구단 거꾸로 출력

# for i in range(9,0,-1):
#     print(f'# {i}단 #')
#     for j in range(9,0,-1):
#         print("{0} x {1} = {2}".format(i,j,i*j))
#

i = 9
while i > 0 :
    print(f"# {i}단 #")
    j = 9
    while j > 0 :
        print("{0} x {1} = {2}".format(i,j,i*j))
        j -= 1
    i -= 1