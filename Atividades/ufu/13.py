
numeros = []

numero = int(input("Qual número deseja fazer a média? "))
numeros.append(numero)

numero = int(input("Qual outro número deseja? "))
numeros.append(numero)

resposta = ""

while resposta != "Não":
    resposta = input(f"Deseja adicionar mais números?(Sim ou Não) ")
    resposta = resposta.title()

    if resposta != "Não":
        numero = int(input("Então escreva seu número "))
        numeros.append(numero)

media = 0
quantidade = 0
for x in numeros:
    media = x + media
    quantidade += 1

media = int(media/quantidade)
print(f"A média aritimética de seus números é: {media}")
