"""
Listas Aninhadas (Nested Lists)

Em outras linguagens de programação temos:

- Unidimensionais (Arrays/Vetores)
- MUltidimensionais (Matrizes)

Em Python, as listas fazem esse serviço


# Exemplos =============================================================================================================

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)

# Acessando os dados ===================================================================================================

listas = [[1, 2 , 3], [4, 5, 6], [7, 8, 9]]

print(listas[0])
print(listas[0][1])  # 2
print(listas[2][1])  # 8


# Iterando com loops ===================================================================================================

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in listas:
    print(lista)

for lista in listas:
    for numero in lista:
        print(f'{numero}', end=' ')

# Iterando com List Comprehension ======================================================================================

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]
"""

# Gerando taubuleira/matriz 3x3 ========================================================================================

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 6)]
# O primeiro for gera os elementos e o segundo gera cada lista, ou seja, 3 por 5

print(tabuleiro)

# Gerando Jogadas para o jogo da velha =================================================================================

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
# Para cada nnumero do range(1, 21) se ele for positivo (if numero % 2 == 0) printar 'X' se não printar 'O'
# Fazer isso para cada valor in range(1, 4)

print(velha)

# Gerando valor iniciais ===============================================================================================

print([['*' for i in range(1, 4)] for j in range(1, 4)])