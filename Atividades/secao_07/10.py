contador = 0
lista = []

while contador < 15:
    numero = int(input(f"Digite o valor da nota do {contador + 1}º aluno"))
    contador += 1
    lista.append(numero)

soma = 0

for x in lista:
    soma = soma + x


print(f'A média das notas dos alinos é {soma / 15}')