"""
Any e All

All() -> Retorna true se todos elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplos All() =======================================================================================================

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # Todos os números são verdadeiros? True

nomes = ['Carcos', 'Carlo', 'Carla', 'Cintia']

print(all(nome[0] == 'C' for nome in nomes))  # True

# Printar cada numero na lista [4, 1, 2, 5, 8] se esse numero for par
print(all([num for num in [4, 1, 2, 5, 8] if num % 2 == 0]))  # True

========================================================================================================================

Any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio,retorna false

# Exemplos Any() =======================================================================================================

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, 0, 0, False, {}, [], ()]))  # False

print(any([0, 0, 0, False, {}, [], (), 1]))  # True

nomes = ['Carcos', 'Carlo', 'Carla', 'Cintia']

print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([num for num in [4, 1, 2, 5, 8] if num % 2 == 0]))  # True

print(any([num for num in [0, 1, 2, 5] if num == 0]))  # False
"""



