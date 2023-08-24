contador = 0
lista = []

while contador < 10:
    numero = int(input(f"Digite o valor da {contador + 1}º posição do vetor:"))
    contador += 1
    lista.append(numero)

max = max(lista)
posicao = lista.index(max)

print(f'O maior valor dessa lista é {max} e está na posição {posicao + 1} ')
