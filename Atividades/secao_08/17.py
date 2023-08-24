"""
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne
a soma dos N números inteiros existente entre eles
"""


lista1 = []
contador = 0

while contador < 2:
    x = int(input(f'Digite o {contador + 1}º número que deseja'))
    lista1.append(x)
    contador += 1

num1, num2 = lista1


def maior_ou_menor(a, b):
    if a >= b:
        diferenca(a, b)
    elif a <= b:
        diferenca(b, a)   # Troca de lugar pra não haver número negativo na contagem


def diferenca(c, d):
    lista = []
    conta = c - d
    cont = 0
    while cont < conta:
        lista.append(cont+1)
        cont += 1

    print(sum(lista))


maior_ou_menor(num1, num2)