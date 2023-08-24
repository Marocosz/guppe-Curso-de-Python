import math

num = int(input('Digite seu número aqui:'))

if num > 0:
    numr = math.sqrt(num)
    print(f'A raiz quadrada de seu número é: {numr:.2f}')
else:
    numq = num ** 2
    print(f'Seu número elevado ao quadrado é: {numq:.2f}')
