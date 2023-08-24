"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros
cada. Crie um novo vetor denominado C calculando C =A - B. Mostre na tela os dados
do vetor C.
"""


contador = 0
a = []

while contador < 10:
    numero = int(input(f"Digite o valor do vetor na {contador + 1}º posição dos primeiros números"))
    contador += 1
    a.append(numero)

contador = 0
b = []

while contador < 10:
    numero = int(input(f"Digite o valor do vetor na {contador + 1}º posição dos segundos números"))
    contador += 1
    b.append(numero)

c = []
cont = 0

while cont < 10:
    h = int(a[cont]) - int(b[cont])
    c.append(h)
    cont += 1




print(f'A diferença de cada lista é {c}')