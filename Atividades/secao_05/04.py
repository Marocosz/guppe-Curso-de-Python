import math

num = int(input('Digite seu número aqui:'))

if num > 0:
    numq = num ** 2
    print(f'O quadrado de seu número é: {round(numq, 2)}')
    numr = math.sqrt(num)
    print(f'A raiz quadrada de seu número é: {round(numr, 2)}')
else:
    print('Error')