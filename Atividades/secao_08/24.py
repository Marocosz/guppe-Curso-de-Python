"""
Escreva uma função que gera um triängulo de altura e lados n e base 2'n-1. Por exem-
plo, a saída para n = 6 seria:

      *
     ***
    *****
   *******
  *********
 ***********

"""

num = int(input('Digite a altura do triangulo que deseja: '))


def triangulo(n):
    for x in range(1, n + 1):  # coloca pra iniciar no 1 para não haver uma linha de saída em branco
        var = "*" * x  # Seria a parte da direita do triangulo
        vare = "*" * (x - 1)  # Seria a parte da esquerda do triangulo
        esp = " " * (n - x)  # são os 'espaços' para alinhar o triangulo
        print(esp + vare + var)


triangulo(num)
