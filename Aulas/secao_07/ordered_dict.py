"""
Módulo Collections - Ordered Dict

# Em um dicionário a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for chave, valor in dicionario.items():
    print(f'Chave: {chave} e Valor: {valor}')


Ordered Dict -> É um dicionário que nos garante a ordem de inserção dos elementos

    # Importando ---------------------------------------------------------------------------------------------------

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
"""
from collections import OrderedDict

    # Entendendo a diferença entre Dict e Ordered Dict ----------------------------------------------------------------

# Dicionários Comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True ja que a ordem não importa

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False, pois no Ordered a ordem é importante




