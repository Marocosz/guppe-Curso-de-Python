"""
Módulo Collections - Named Tuple

# Recap Tupla

tupla = (1, 2, 3)
print(tupla)

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

    # Importando --------------------------------------------------------------------------------------------

from collections import namedtuple

# Após o import, precisamos definir o nome e parâmetros.

# Forma 01 - Declaração Named Tuple

cachorro1 = namedtuple('Cachorro', 'Idade, Raça, Nome')

# Forma 02 - Declaração Named Tuple

cachorro2 = namedtuple('Cachorro', 'idade Raça Nome')

# Forma 03 - Declaração Named Tuple

cachorro3 = namedtuple('Cachorro', ['Idade', 'Raça', 'Nome'])

# Acessando os dados

    # Forma 01 -------------------------------------------------------------------------------------------------------

ray = cachorro1(Idade=2, Raça ='Chow-chow', Nome='Ray')
print(ray)

print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome

# Forma 02

print(ray.Idade)
print(ray.Raça)
print(ray.Nome)