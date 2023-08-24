contador = 0
auxiliar = 0
lista = []

while contador < 10:
    numero = int(input(f"Digite o valor da {contador + 1}º posição do vetor:"))
    contador += 1
    lista.append(numero)

max = max(lista)
min = min(lista)

print(f'O maior valor dessa lista é {max} e o menor {min}')