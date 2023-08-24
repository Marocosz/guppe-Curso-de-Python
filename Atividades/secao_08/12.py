

def somad(a):
    total = 0
    if a > 0:
        while a != 0:
            total += a % 10
            a = a // 10

        return f'A soma dos algarismo é {total}'
    else:
        return 'Número invalido'


print(somad(234))