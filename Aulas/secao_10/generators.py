"""
Generators

É basicamente Tuple Comprehension

nomes = ['Carlos', 'Carla', 'Cristina', 'Cassiano', 'Vanessa]

print(any([nome[0] == 'C' for nome in nomes]))

# Exemplo ==============================================================================================================

nomes = ['Carlos', 'Carla', 'Cristina', 'Cassiano', 'Vanessa']

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator

res1 = (nome[0] == 'C' for nome in nomes)
print(type(res1))

# Getsizeof ============================================================================================================

from sys import getsizeof
# getsizeof retorna a quantidade em memória do elemento passado como parâmetro

print(getsizeof('Marcos'))
print(getsizeof(('Marcos Rodrigues')))
print(getsizeof(92))
print(getsizeof(True))
print(getsizeof(12031212312312312312312))

# Diferença List Comprehension e Generator =============================================================================

from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])

generator_comp = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(generator_comp)

# Assim podemos ver a diferença dos dois, onde o generator ocupa bem menas memória que o list comprehension
"""

from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])

generator_comp = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(generator_comp)