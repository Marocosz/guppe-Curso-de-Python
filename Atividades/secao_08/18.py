"""
18. Faça uma função que receba por parámetro dois valores X e 2. Calcule e retorne o
resultado de X elevado a Z para o programa principal. Atenção não utilize nenhuma função pronta
de exponenciaçao.
"""


lista1 = []
contador = 0

while contador < 2:
    if contador == 0:
        x = int(input(f'Digite a base da exponenciação'))
        lista1.append(x)
        contador += 1
    elif contador == 1:
        x = int(input(f'Digite o expoente'))
        lista1.append(x)
        contador += 1

num1, num2 = lista1


def exponenciacao(x, z):
    return x ** z


print(exponenciacao(num1, num2))