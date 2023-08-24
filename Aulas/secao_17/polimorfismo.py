"""
Polimorfismo - POO

Polis -> Muitas
Morfis -> Formas

Polimorfismo -> Se comportar de várias formas

Quando reimplementamos um método presente na Classe Pai, nas Classes Filhas, estamos realizando uma sobreescrita
de métodos (Overriding)

O overriding é a melhor representação do polimorfismo



"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):  # Método abstrato, cujo precisa ser reimplementado nas classes filhas
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} faz au au')



class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} faz miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} faz tssss')


felix = Gato('Felix')
felix.comer()
felix.falar()

toto = Cachorro('Toto')
toto.comer()
toto.falar()

mikey = Rato('Mikey')
mikey.comer()
mikey.falar()
