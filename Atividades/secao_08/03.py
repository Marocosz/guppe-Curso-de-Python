def ver_n(a):
    if a < 0:
        a = -1
    elif a > 0:
        a = 1
    elif a == 0:
        a = 0

    return a


print(ver_n(2))
print(ver_n(-5))
print(ver_n(0))