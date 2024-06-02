num = [3,-5,12,-6,90,32,45]

minusNum = list(filter(lambda x:x<0,num))

print(minusNum)

plusNum = [x for x in num if x>0]
print(plusNum)