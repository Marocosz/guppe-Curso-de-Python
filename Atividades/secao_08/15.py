"""
Crie um programa que receba tres valores (obrigatoriamente maiores que zero), repre-
sentando as medidas dos tres lados de um triangulo. Elabore funçoes para:

(a) Determinar se eles lados formam um triängulo, sabendo que:

    .O comprimento de cada lado de um triängulo é menor do que a soma dos outros
dois lados.

(b) Determinar e mostrar o tipo de triàngulo, caso as medidas formem um triàngulo.
Sendo
que:

    Chama-se equilátero o triàngulo que tem três lados iguais.

    Denominam-se isósceles o triängulo que tem o comprimento de dois lados
    iguais.

    Recebe o nome de escalenoo triângulo que tem os três lados diferentes.
"""


lista = []
contador = 0
while contador < 3:
    a = input(f'Digite a medida do {contador+1}º lado do triângulo')
    lista.append(a)
    contador += 1

num1, num2, num3 = lista


def forma_triangulo(a, b, c):
    if a > b + c:
        return 'Essas medidas não são de um triângulo'
    elif a > b + c:
        return'Essas medidas não são de um triângulo'
    elif a > b + c:
        return 'Essas medidas não são de um triângulo'
    else:
        return triangulo(num1, num2, num3)


def triangulo(d, e, f):
    if d == e == f:
        return 'É um triângulo equilátero'
    elif d == e or e == f or d == f:
        return 'É um triângulo isósceles'
    elif d != e != f:
        return 'É um triângulo escaleno'


print(forma_triangulo(num1, num2, num3))


