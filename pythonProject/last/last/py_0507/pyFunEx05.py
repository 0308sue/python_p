#매개변수 딕셔너리 형태 dic_func(dream = 7, 일이칠 = 9, wish = 6)
def dic_func(**para):
    for k in para.keys():
        print("%s --> %d"%(k,para[k]))

dic_func(dream = 7, 일이칠 = 9, wish = 6)