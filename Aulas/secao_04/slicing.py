"""
Slicing de iteráveis

Slincing -> Quer dizer enlaçar, ou seja, pegar determinados valores com base nos índices de iteráveis

usamos: [inicio:final:passo]
"""

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(lista1[1:3])  # [2, 3] # Pega os números dos índices 1 a 3, não contando o '3'
print(lista1[0:3])  # [1, 2, 3]
print(lista1[0::2])  # Pega toda a lista de 2 em 2, ou seja: [1, 3, 5, 7, 9, 11, 13, 15]
print(lista1[6::2])  # Pega desde o índice 6 e vai até o final com passo 2: [7, 9, 11, 13, 15]
print(lista1[8:0:-2])  # do índice 8 ao 0, é para pegar de -2 em -2: [9, 7, 5, 3]
print(lista1[-5])  # Utilizando negativo, pegamos do final ao início: 12

# Slicing múltiplo =====================================================================================================

lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

print(lista2[1][2])  # irá pegar o índice '2' do índice '1' da lista2, ou seja: 6
print(lista2[1][0:3])  # Do índice 1 pega, o índice 0 ao 3: [4, 5, 6]
print(lista2[::][4])  # De todos os índices, é para pegar o índice 4: [13, 14, 15]
print(lista2[3][-1])  # Do índice 3 pega o índice '-1': 12
print(lista2[2][::])  # Do índice 2 pega todos os índices: [7, 8, 9]



