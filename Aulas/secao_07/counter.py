"""
Módulo Collections - Counter  (Contador)

Collections -> High-Performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor
a quantidade de ocorrências desse elemento

    # Realizando o Import ----------------------------------------------------------------------------------------------

from collections import Counter  # Importando uma biblioteca

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 1, 2, 1, 5, 5, 3, 3, 3, 3, 4, 4, 4, 4,]

    # Utilizando o counter --------------------------------------------------------------------------------------------

# Exemplo 01

res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 4, 3: 4, 4: 4, 5: 2})
# Para cada elemento da lista, o counter criou uma chave e como valor colocou a quantidade de ocorrências de cada chave
# E percebe-se que organizou em ordem decrescente de ocorrências

# Exemplo 02

print(Counter('Marcos Rodrigues'))
# Counter({'r': 2, 'o': 2, 's': 2, 'M': 1, 'a': 1, 'c': 1, ' ': 1, 'R': 1, 'd': 1, 'i': 1, 'g': 1, 'u': 1, 'e': 1})
"""

from collections import Counter

# Exemplo 03

texto = """ Lorem ipsum dolor sit amet. Et debitis error et excepturi autem ad nisi incidunt et minima nemo ab dolorem
 maiores vel odit quas ab dolorum corrupti. Non possimus facere quo nulla iure sit laudantium quidem ex fugiat maiores 
 eos repellendus magni vel velit dolor. Qui amet accusamus hic commodi mollitia est debitis ipsa hic numquam 
 consectetur in omnis natus. In sapiente quia est beatae facere est tempore reprehenderit.
"""

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

    # Encontrando as 5 palavras mais comuns no texto -------------------------------------------------------------------

print(res.most_common(5))
