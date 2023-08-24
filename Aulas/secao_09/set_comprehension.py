"""
Set Comprehension
"""

numeros = {x ** 2 for x in range(1, 10)}

print(numeros)


numeros = {x: x**2 for x in range(1, 5)}

print(numeros)


letras = {letra for letra in 'Marcos Rodrigues'}

print(letras)