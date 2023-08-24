"""
Considere um vetor A com 11 elementos onde Al < A2 < A6> AT
Al, ou seja, está ordenado em ordem crescente ate o sexto elemento, e a partir
desse elemento está ordenado em ordem decrescente. Dado o vetor da questão anterior,
proponha um algoritmo para ordenar os elementos.
"""


contador = 0
lista = []

while contador < 11:
    numero = int(input(f"Digite o valor do vetor na {contador + 1}º posição"))
    contador += 1
    lista.append(numero)

lista.sort()

contador = 0
lista1 = []

while contador < 6:
    contador += 1
    lista1.append(lista[contador - 1])

lista.sort(reverse = True)

contador = 0
lista2 = []

while contador < 5:
    contador += 1
    lista2.append(lista[contador - 1])

lista3 = lista1 + lista2
print(lista3)