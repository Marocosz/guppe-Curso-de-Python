"""
Escreva um codigo que apresente a classe Retangulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e
perimetro. O método imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a área de um retângulo é obtida pela fórmula
(comprimento * largura) e o perímetro por (2 * comprimento) +(2 * largura).
"""


class Retangulo:

    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = 0
        self.__perimetro = 0

    def calcularArea(self):
        self.__area = self.__largura * self.__comprimento
        print('Área calculada!')

    def calcularPerimetro(self):
        self.__perimetro = (2 * self.__largura) + (2 * self.__comprimento)
        print('Perímetro calculado!')

    def imprimir(self):
        print(f'Comprimento: {self.__comprimento}\n'
              f'Largura: {self.__largura}\n'
              f'Área: {self.__area}\n'
              f'Perímetro: {self.__perimetro}')


ret1 = Retangulo(6, 6)
ret1.imprimir()
ret1.calcularPerimetro()
ret1.calcularArea()
ret1.imprimir()