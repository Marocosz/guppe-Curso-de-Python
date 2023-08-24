"""
Loop -> Estrutura de repetição
for -> Uma dessas estruturas

Utílizamos Loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
    -String
        nome = 'Marcos'
    -Lista
        lista = [1, 2, 3, 4, 5]
    -Range
        numeros = range(1, 10)

# Quando n precisamos de um valor, podemos descartar ele usando '_'.


nome = 'Marcos'
lista = [1, 2, 3, 4, 5]
ran = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:   # Para cada letra dentro cima de 'nome'(interável), imprimir a letra
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
# range(valor inicial, valor final)
# No range, o valor final não é incluso
for numero in range(1, 10):
    print(numero)

print('==============================================================================================')

enumerate: 

((0, 'M'), (1, 'a'), (2, 'r'), (3, 'c')...)  # Sendo 0,1,2... os indices e M,a,r... as letras

for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

print('==============================================================================================')

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd):
    print(f'Imprimindo {n}')

print('==============================================================================================')

soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

print('==============================================================================================')

for letra in nome:
    print(letra, end='')  # ('end='') Serve para que o print seja todo mostrado em uma linha, e não um caractere por linha

# Tabela de Emojis para códigos: https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F601
# Modificado pelo Python: U0001F601
"""

emoji = '\U0001F601'   # Necessita do \ para idenficar como emoji

for _ in range(3):
    for num in range(11):
        print(f'{emoji * num}')

for x in range(9):
    print(x)
else:
    print('asdasd')

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for list in list_of_lists:
    print(list)

for list in list_of_lists:
    for x in list:
        print(x, end='')
