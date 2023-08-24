numero = [int(input('Digite um número: ')) for n in range(10)]

denominador = list(elemento for elemento in numero if elemento > 0)

soma = sum(elemento for elemento in numero if elemento > 0)

lista1 = denominador

media = soma / len(denominador)

print(f'A média é {media}')