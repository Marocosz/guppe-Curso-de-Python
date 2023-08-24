"""
Debuggar com f-strings

"""

nome: str = 'Marcos Rodrigues'

# Com f-strings ========================================================================================================

# Utilizando '=' na frente da variável ou função que esteja fazendo na variável temos:

print(f'{nome=}')  # nome='Marcos Rodrigues'
print(f'{nome.upper()=}')  # nome.upper()='MARCOS RODRIGUES'
print(f'{nome.upper()[::-1]=}')  # nome.upper()[::-1]='SEUGIRDOR SOCRAM'

# E Com isso, podemos testar resultados de forma mais visível
