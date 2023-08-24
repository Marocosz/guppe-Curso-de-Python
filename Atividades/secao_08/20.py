"""
Faça um algoritmo que receba um numero inteiro positivo n e calcule o seu fatorial, n!.
"""

num = int(input('Digite o número que deseje fatorar'))


def fatorar(x):
    total = 1
    for n in range(x):
        total = total * (n + 1)

    return total


print(fatorar(num))