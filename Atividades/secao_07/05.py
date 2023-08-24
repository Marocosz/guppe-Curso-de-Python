contador = 0
auxiliar = 0
lista = []

while contador < 10:
    numero = int(input(f"Digite o valor da {contador + 1}º posição do vetor:"))
    contador += 1
    lista.append(numero)

for valor in lista:
    if valor % 2 == 0:
        auxiliar += 1

print(f"O vetor possui {auxiliar} valores pares")