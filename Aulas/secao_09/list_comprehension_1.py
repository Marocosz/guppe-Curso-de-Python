"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a aprtir de
outro iterável

# Sintaxe da List Comprehension ========================================================================================

[dado for dado in iterável]
"""
# Exemplo 01 ===========================================================================================================

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]  # Para cada número da lista, multiplica-lo por 10

print(res)

# A primeira parte: for numero in numeros = para cada 'numero' da lista
# A segunda parte: numero * 10 = multiplicar 'numero' por 10
"""
# Exemplo 02 ===========================================================================================================

numeros = [1, 2, 3, 4, 5]


def funcao(valor):
    return valor * 2


res = [funcao(numero) for numero in numeros]  # Para cada 'numero' da lista numeros inserir na função funcao

print(res)

# List Comprehension vs Loop ===========================================================================================

# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension

numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)

# Outro Exemplo ========================================================================================================

# 01 ===================================================================================================================

nome = 'Marcos Rodrigues'

print([letra.upper() for letra in nome])

# 02 ===================================================================================================================

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

# 03 ===================================================================================================================

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())  # Trocar a primeira letra pela primeira letra em caixa alta
    return nome


print([caixa_alta(amigo) for amigo in amigos])

# 04 ===================================================================================================================

print([numero * 3 for numero in range(1, 10)])

# 05 ===================================================================================================================

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 06 ===================================================================================================================

print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""



