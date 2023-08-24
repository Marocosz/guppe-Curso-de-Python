num = int(input('Digite um número inteiro positivo:\n'))

if num > 0:
    u = int(num // 1 % 10)
    d = int(num // 10 % 10)
    c = int(num // 100 % 10)
    m = int(num // 1000 % 10)
    soma = u + d + c + m
    print(f'A soma dos algarismos é {soma}')
else:
    print('Número inválido.')