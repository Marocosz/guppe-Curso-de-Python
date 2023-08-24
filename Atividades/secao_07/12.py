contador = 0
lista = []
soma = 0

while contador < 5:
    numero = int(input(f"Digite o valor do vetor na {contador + 1}º posição"))
    contador += 1
    lista.append(numero)

print('Os valores dos vetores são:')
for x in lista:
    print(f' {x}, ', end='')

for x in lista:
    soma = soma + x

print(f'e a sua média é {soma / 5}, sendo o {max(lista)} maior número e o {min(lista)} o menor número')