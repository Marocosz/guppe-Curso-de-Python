# Leia uma matriz 4x4, conte e escreve quantos valores maiores que 10 ela possui

matriz = [[12, 21, 4, 6],
          [5, 23, 98, 2],
          [1, 35, 5, 6],
          [23, 67, 3, 10]]

lista = []

for x in matriz:
    for y in x:
        if y > 10:
            lista.append(y)


print(f'A matriz tem {len(lista)} números maiores que 10, sendo eles: {lista}')

