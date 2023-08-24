"""
Escreva uma funçao que gera um triangulo lateral de altura 2'n-1 en largura. Por exem-
plo, a saida para n = 4 seria:
*
**
***
****
***
**
*
"""


num = int(input('Digite a quantidade de linhas que deseja'))


def estrela(x):
    for n in range(1, x + 1):
        var = "*" * n
        print(var)

    for n in range(x, 0, -1):
        var = "*" * n
        print(var[0:n-1])



estrela(num)