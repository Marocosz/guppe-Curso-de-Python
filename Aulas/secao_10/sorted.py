"""
Sorted

Podemos utilizar o sorted() com qualquer iterável, diferente do sort() sendo apenas em listas

OBS: O sorted SEMPRE retorna uma lista com os elementos do iterável ordenado, porém não modifica o iterável

# Exemplo ==============================================================================================================

numeros = [6, 5, 2, 1, 9, 7]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

# Exemplo com parãmetro ================================================================================================

numeros = [6, 5, 2, 1, 9, 7]

print(sorted(numeros, reverse = True))  # Ordena do maior para o menor

# Exemplo mais Complexo ================================================================================================

usuarios = [
    {'Username': 'Samuel', 'Tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'Username': 'Carla', 'Tweets': ['Eu amo meu cachorro', 'Eu gosto de nadar'], 'cor': 'amarelo', 'música': 'rock'},
    {'Username': 'Bob123', 'Tweets': []},
    {'Username': 'Jeff', 'Tweets': ['Eu cuido da minha vó'], 'cor': 'preto'},
    {'Username': 'Marcos', 'Tweets': []},
    {'Username': 'Heloísa', 'Tweets': ['Eu adoro jogar', 'Tirei nota 10']},
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario['Username']))  # Ordem alfabética conforme o 'Username'

print(sorted(usuarios, key=lambda usuario: len(usuario['Tweets'])))  # Ordem de quantidade de 'Tweets'
"""

# Exemplo ==============================================================================================================

musicas = [
    {'Título': 'Thunderstruck', 'Tocou': 3},
    {'Título': 'Love Of My Life', 'Tocou': 12},
    {'Título': 'Back in Black', 'Tocou': 1231},
    {'Título': 'Breaktruhf', 'Tocou': 25},
    {'Título': 'Bohemian Rhapsody', 'Tocou': 167},
]

print(sorted(musicas, key=lambda musica: musica['Tocou']))  # Ordena da menos tocada para mais tocada

print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))  # Ordena da mais tocada para menos tocada
