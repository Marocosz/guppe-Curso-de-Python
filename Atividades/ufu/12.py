print("Digite 3 números que deseje fazer a média aritimética: ")
contador = 0
medialist = []
while contador != 3:
    numero = int(input("Digite o número:"))
    contador += 1
    medialist.append(numero)

media = 0

for x in medialist:
    media = x + media

media = media/3

print(f"A média de seus números é: {media} ")