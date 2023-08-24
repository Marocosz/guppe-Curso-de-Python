"""
Reduce

Usa-se reduce() a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() só se extremamente necessário, pois utilizando loop for é mais legível

Para entender o Reduce()

Imagina que você tem uma coleção de dados:

dados = [a1, a2, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y)
    return x * y

A função reduce() funciona da seguinte forma:

    Passo 1: res1 = f(ai, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3)
    Passo 3: res3 = f(res2, a4)
    Passo4: ...

E no final ela retornará o resultado final

Poderiamos ver a função reduce() como:

funcao(funcao(fucao(a1, a2), a3), a4) ...), an)
"""

# Exemplo ==============================================================================================================

from functools import reduce

dados = [1, 2, 3, 12, 213, 29, 98, 12, 21, 76, 23, 95, 72]

# Para utilizaar Reduce() precisamso de uma função que receba dois parâmetros

mult = lambda x, y: x * y

res = reduce(mult, dados)

print(res)