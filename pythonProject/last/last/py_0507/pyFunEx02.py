def multi(v1,v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2

    retList.append(res1)
    retList.append(res2)

    return retList

mList = multi(10,20)
print(mList)