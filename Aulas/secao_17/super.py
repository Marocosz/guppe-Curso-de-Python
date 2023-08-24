"""
Método Super() - POO

O Método Super() se refere á super classe


"""


class Animal:  # Super Classe

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):  # Classe Específica

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


gato1 = Gato('Tico', 'Felino', 'Angorá')

gato1.faz_som('Miau')