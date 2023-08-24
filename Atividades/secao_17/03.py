"""
3) Escreva um código lado, áreae perimetro e, os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
que apresente a classe Quadrado, com atributos
cálculos e colocar os valores nos atributos area e perimetro. O método imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de
um quadrado é obtida pela förmula (lado * lado) e o perímetro por (4 * lado).
"""


class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado
        self.__perimetro = 4 * lado

    def imprimir(self):
        return f'É um quadrado com lado: {self.__lado}, area: {self.__area}, perimetro: {self.__perimetro}'


quadrado1 = Quadrado(23)
print(quadrado1.imprimir())