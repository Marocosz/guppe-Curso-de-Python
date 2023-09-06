"""
Map

Com map fazemos mapeamento de valores para função

# Para fixar ===========================================================================================================

# Temos dados iteraveis: dados = a1, a2..., an

# Temos uma função: def f(x)

# Utilizando map: map(f, dados)

# O map irá 'mapear' cada elemento de 'dados' e aplicar eles na função 'f'

# O Map Object: f(a1), f(a2), f(...), f(an)

# Em função ===========================================================================================================

import math


def area(r):
    return math.pi * (r ** 2)
    # Calcula a área de um círculo com raio 'r'   # Docstring


print(area(5.3))

raios = [2, 5, 10, 23, 12, 8]

# Forma comum ==========================================================================================================

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma com Map ========================================================================================================

# Map é uma função que recebe dois parâmetros, primeiro a função e o segundo o iterável

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma map com lambda =================================================================================================

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS!!!!! Após utilizar a função map() pela primeira vez, ele zerará, não tendo como usar novamente
"""
# Exemplo ==============================================================================================================

cidades = [('Berlim', 29), ('Cairo', 36), ('São Paulo', 19), ('Tokyo', 27), ('Londres', 22)]


c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)

# Criar uma tupla, onde vai ter o primeiro elemento:(dado[0])
# e o segundo elemento irá ser: (9/5) * dado[1] + 32

print(list(map(c_para_f, cidades)))  # Utilizando map damos para o lambda que dado será cada elemento da lista cidades

print(c_para_f(('Alo', 10)))
