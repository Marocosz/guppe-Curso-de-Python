contador = 0
lista = []
alarme = 0

while contador < 6:
    numero = int(input(f"Digite o valor par da {contador + 1}º posição do vetor:"))
    contador += 1
    lista.append(numero)

for x in lista:
    if x % 2 != 0:
        alarme = 1

if alarme == 1:
    print('Digite apenas valores pares')

else:
    lista.reverse()

    print(f'A lista invertida é {lista}')