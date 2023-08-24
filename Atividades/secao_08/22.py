"""
Crie uma funçã0 que receba como parámetro um valor inteiro e gere como saída n linhas
com pontos de exclamação, conforme o exemplo abaixo (para n= 5)
!
!!
!!!
!!!!
!!!!!
"""

num = int(input('Digite a quantidade de linhas que deseja'))


def exclamacao(x):
    for n in range(x + 1):
        print (f'{"!" * n}')


exclamacao(num)