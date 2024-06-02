a = 20

def func1():
    global a
    a = 10
    print('func1 => %d'%a)

def func2():
    print('func2 => %d' % a)

func1()
func2()

