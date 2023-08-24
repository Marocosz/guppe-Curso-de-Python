"""
Tipo Booleano

2 constantes, Verdadeiro ou Falso (True, False) # Sempre inicial maiúscula
"""

ativo = False
print(ativo)

"""
Operações Básicas

- Negação (not):

Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso
Se for falso, o resultado será verdadeiro
Ou seja, sempre o contrário

"""

print(not ativo)
logado = False

"""
- Ou (or):

É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True = True
True or False = True
False or True = True
False or False = False
"""

print(ativo or logado)

"""
- E (and):

Também é uma operação binária, ou seja, depende dos dois valores. Ambos os valores
devem ser verdadeiros

True and True = True
True and False = False
False and True = False
False and False = False

"""