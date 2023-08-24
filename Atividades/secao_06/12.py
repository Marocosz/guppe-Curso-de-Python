n = int(input('Digite um número inteiro positivo:'))

for numero in range(n, -n, -1):
    if numero > -1:
        print(f'{numero} ', end='')
