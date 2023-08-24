"""
Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado
da seguinte série:
S=2/4+5/5+ 10/6 +.+(N²+1)/(N +3)
"""

num = int(input('Digite o número que deseja efetuar a operação'))


def operacao(x):
    for n in range(1, x):
        soma = ((x**2)+n)/(x+(n+2))

    return soma


print(operacao(num))