"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas

A função reverse() só funciona em listas, reversed() funciona em qualquer iterável, com a função de inverter

A função reversed() retorna um tipo iterável chamado 'list reverse iterator'

# Exemplo ==============================================================================================================

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# convertido

print(list(reversed(lista)))

# Exemplo String =======================================================================================================

for letra in reversed('Marcos Rodrigues'):
    print(letra, end='')

print('')

# Sem utilizar for

print(''.join(list(reversed('Marcos Rodrigues'))))

# Utilizando slice

print('Marcos Rodrigues'[::-1])

# Exemplo loop for =====================================================================================================

for n in reversed(range(0, 11)):
    print(n)

# Sem reversed

for n in range(10, -1, -1):
    print(n)
"""

