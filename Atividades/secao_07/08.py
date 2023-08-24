contador = 0
lista = []

while contador < 6:
    numero = int(input(f"Digite o valor da {contador + 1}º posição do vetor:"))
    contador += 1
    lista.append(numero)

lista.reverse()

print(f'A lista invertida é {lista}')