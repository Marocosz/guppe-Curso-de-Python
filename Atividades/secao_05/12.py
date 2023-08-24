import math

num = int(input('Digite seu número inteiro aqui:'))
numl = math.log2(num)

if num > 0:
    print(f'O logaritimo do seu número é {round(numl, 2)}.')
else:
    print('Número Inválido')
