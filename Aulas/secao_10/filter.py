"""
Filter

Filter() - Serve para filtrar dados de uma determinada coleção

# Assim como o map, o valor só pode ser utilizado uma vez

Map -> Recebe uma função e um iterável, e retorna um objeto mapeando a função para cada elemento do iteravel
Filter -> Recebe uma função e um iterável, e retorna um objeto filtrando apenas os elementos de acordo com a função

# Exemplo ==============================================================================================================

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados com a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map, a filter recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

# Para cada valor em 'dado', ele entrará na lambda, assim saindo true or false, e a função filter entrega os true
# Dessa forma, utilizando filter() ele filtra os 'dados' e retorna conforme a função, no caso o lambda

# Exemplo ==============================================================================================================

paises = ['', 'Argentina', 'Brasil', '', 'Chile', 'Dinamarca', '', '', 'Equador', 'Venezuela']
print(paises)

res = filter(None, paises)  # Dessa forma os dados vazios são filtrados
print(list(res))

# Outra forma ==========================================================================================================

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Exemplo Complexo =====================================================================================================

usuarios = [
    {'Username': 'Samuel', 'Tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'Username': 'Carla', 'Tweets': ['Eu amo meu cachorro', 'Eu gosto de nadar']},
    {'Username': 'Bob123', 'Tweets': []},
    {'Username': 'Jeff', 'Tweets': ['Eu cuido da minha vó']},
    {'Username': 'Marcos', 'Tweets': []},
    {'Username': 'Heloísa', 'Tweets': ['Eu adoro jogar', 'Tirei nota 10']},
]

# Filtrar os úsuarios inativos

# Forma 01
inativos = list(filter(lambda u: len(u['Tweets']) == 0, usuarios))

print(inativos)

# Forma 02
inativos = list(filter(lambda u: not u['Tweets'], usuarios))

print(inativos)

"""

# Filter e Map =========================================================================================================

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo: 'Sua instrutora é: 'Nome'', desde que cada nome tenha - de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)