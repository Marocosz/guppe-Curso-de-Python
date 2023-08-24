"""
Dictionary Comprehension

Pense no seguinte:

    Se quisemos criar um alista fazemos:

    lista = [1, 2, 3, 4]

    Se quisermos criar uma tupla:

    tupla = (1, 2, 3 ,4)

    Se quisermos criar um conjunto:

    conjunto = {1, 2, 3, 4}

    Se quisermos criar um dicionário:

    dic = {'a': 1, 'b': 2, 'c': 3}

# Sintaxe:

{chave:valor for iterável}


# Exemplos =============================================================================================================

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave + '2': valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


# Exemplos =============================================================================================================

numeros = [1, 2, 3, 4]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

# Exemplos =============================================================================================================

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)

"""

# Exemplo com lógica condicional =======================================================================================

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)