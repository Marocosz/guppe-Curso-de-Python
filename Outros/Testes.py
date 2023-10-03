x = 5
def func1():
    global x
    print('aaa')
    x = 2
    return x

a = func1()
print(a)
print(a)
print(a)