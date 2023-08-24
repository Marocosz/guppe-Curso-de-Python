"""
Zip

# zip() -> Cria um iterável (zip object) que agrega elemento de cada um dos dois iteráveis passado com oentrada em pares
# Ele pega um elemento de cada iterável e forma pares ou trios ou a quantidade que der

# Exemplos =============================================================================================================

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 21]
lista3 = [7, 8, 9, 10, 11, 12]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))
print(list(zip1))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]  # Ele pega um elemento de cada iterável e forma pares
print(dict(zip1))  # Não há nada, pois assim como outras funções ele só pode ser utilizado uma vez

zip2 = zip(lista1, lista2)

print(dict(zip2))  # {1: 4, 2: 5, 3: 6}

zip3 = zip(lista1, lista2, lista3)

print(list(zip3))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# OBS: O Zip utiliza como parâmetro o tamanho do menor iterável, isso significa que irá parar de trabalhar quando acabar
# o menor iterável

# Lista de Tuplas ======================================================================================================

dados = [(0, 1), (2, 3), (4, 5), (6, 7)]

print(list(zip(*dados)))  # O '*' serve para desempacotar o iterável
"""

# Exemplo mais complexo ================================================================================================

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carlo']

print(list(zip(alunos, prova1, prova2)))

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}  # dictionary comprehension

# É um dict com o dado[0] (Aluno) e o max entre os dado[1] e dado[2] (prova1 e prova2) para cada dado no zip

print(final)

# Podemos utilizar o map() ======================

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

# Primeiro temos o zip(prova1, prova2) o qual resultará em [(80,98), (91, 89), (78, 53)]

# Utilizando o map ele pegará esse primeiro resultado e jogará no lambda que pegará o max entre cada uma dessas
# duas notas resultantes do zip

# E por último temos um zip de alunos e do resultado, quer ordernará da seguinte forma:
# {'Maria': 98, 'Pedro': 91, 'Carlo': 78}

print(dict(final))