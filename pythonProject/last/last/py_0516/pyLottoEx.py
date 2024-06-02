import random as rd

num = list(range(1,46))
# print(num)

for i in range(5):
    num = list(range(1, 46))
    lottoNum = rd.sample(num,6)
    # print(type(lottoNum))
    print(lottoNum)