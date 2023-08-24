import math

num = int(input('Digite seu número aqui:'))

if num > 0:
    numr = math.sqrt(num)
    print(f'A raiz quadrada de seu número é: {numr:.2f}.')
else:
    print('Número inválido')
