contador = 0
lista = []

while contador < 5:
    numero = int(input(f"Digite o valor do vetor na {contador + 1}º posição"))
    contador += 1
    lista.append(numero)

max = max(lista)
min = min(lista)
maxp = lista.index(max)
minp = lista.index(min)

print(f'O maior número se encontra no vetor {maxp + 1} e o menor no {minp + 1}')
