"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplo ==============================================================================================================

lista = [1, 2, 21, 232, 21, 23]

print(max(lista))  # 232
print(min(lista))  # 1

print(max('a', 'cbs', 'basd', 'd', 'ds', 'dz', 'dss'))
print(min('a', 'cbs', 'basd', 'd', 'ds', 'dz', 'dss'))

# Outros Exemplos ======================================================================================================

nomes = ['Marcos', 'Rodrigues', 'Oliveira', 'Junior', 'Enzo', 'Heloisa', 'Tim', 'Willian']

print(max(nomes))  # Willian
print(min(nomes))  # Tim

print(max(nomes, key=lambda nome: len(nome)))  # Rodrigues
print(min(nomes, key=lambda nome: len(nome)))  # Tim

# Outro Exemplo ========================================================================================================

musicas = [
    {'Título': 'Thunderstruck', 'Tocou': 3},
    {'Título': 'Love Of My Life', 'Tocou': 12},
    {'Título': 'Back in Black', 'Tocou': 1231},
    {'Título': 'Breaktruhf', 'Tocou': 25},
    {'Título': 'Bohemian Rhapsody', 'Tocou': 167},
]

print(max(musicas, key=lambda musica: musica['Tocou']))
print(min(musicas, key=lambda musica: musica['Tocou']))

# Apenaso título

print(max(musicas, key=lambda musica: musica['Tocou'])['Título'])
print(min(musicas, key=lambda musica: musica['Tocou'])['Título'])

# Fazendo isso sem max min e lambda

max = 0
min = 99999999

for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['Título'])

for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['Título'])
"""
