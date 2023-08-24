"""
Entendendo Iterator e Iterables

Iterator ->
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterabel ->
    - Um objeto que irá retornar iterator, quando a função iter() for chamada

"""

# Exemplo ==============================================================================================================

nome = 'Marcos'  # É um iterable, mas não e um interator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não e um interator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # Passamos para o próximo dado do iterator
print(next(it1))
print(next(it1))
print(next(it1))

for letra in nome:
    print(letra)
