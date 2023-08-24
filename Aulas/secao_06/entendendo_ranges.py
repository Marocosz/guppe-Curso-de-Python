"""
Ranges são utilizados para gerar sequências númericas, não de forma aleátoria, mas
de maneira específica

Obs: A contagem tem ínicio no 0, ou seja, se o valor de parada for 10, parará no 9

Formas gerais:

    Forma 1:
    -range(valor_de_parada)
    Obs: O úsario especificando apenas o valor de parada

    Forma 2:
    -range(valor_de_inicio, valor_de_parada)
    Obs: O úsuario especificando valor de inicio e de parada

    Forma 3:
    -range(valor_de_inicio, valor_de_parada, passo)
    Obs: O úsuario especificando o valor de ínicio, de parada e o passo

    Forma 4 (inversa)
    -range(valor_de_inicio, valor_de_parada, -passo)
    Obs: Funciona igual a Forma 3, porém inversamente


# Forma 1:
for num1 in range(11):
    print(num1, end = '')

# Forma 2
for num2 in range(-2, 7):
    print(f' {num2} ', end = '') #end = '' -> Serve para não pular linha por linha, e sim todo código em uma linha

# Forma 3
for num3 in range(1, 20, 2):
    print(num3)

"""

# Forma 4
for num4 in range(10, -21, -1):
    print(num4)