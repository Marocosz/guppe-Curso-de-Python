contador = 0
lista = []
soma = 0
lista2 = []

while contador < 10:
    numero = int(input(f"Digite o valor dos vetores na {contador + 1}º posição"))
    contador += 1
    lista.append(numero)

for x in lista:
    if x > 0:
        soma = soma + x
    else:
        lista2.append(x)

print(f'A soma dos números positivos é {soma}, e a quantidade de números negativos é {len(lista2)}')

