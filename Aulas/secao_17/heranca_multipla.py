"""
Herança Múltipla

Herança Mútipla nada mais é do que a possibilidade de uma classe herdar mais de uma classe
Fazendo com que a classe filha herde todos os atributos e métodos das classes herdadas

 - Há duas maneiras de fazer herança múltipla
    - Por Multiderivação Direta
    - Por Multiderivação Indireta


# OBS: Quando há mais de uma classe herdada, e métodos nomeados igualmente em cada uma delas,
a preferência será da classe herdada primeiramente


# Multiderivação Direta ================================================================================================


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Multiderivação Indireta ==============================================================================================


class Base1:
    pass


class Base2(Base1):
    pass

class Base3(Base2):
    pass


class MultiDerivada2(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta, a classe que realizar
"""


class Animal:  # Super Classe

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def cumprimentar(self):
        return f'O {self.__nome} cumprimentou'


class Aquatico(Animal):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'O {self._Animal__nome} cumprimentou swiiiin'


class Terrestre(Animal):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'O {self._Animal__nome} cumprimentou trrrrrrrtrrrrrrrr'


# Essa classe está herdando diretamente das classes 'Aquatico' e 'Terrestre' e indiretamente da classe 'Animal'
class Pinguin(Terrestre, Aquatico):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)


baleia = Aquatico('Wally', 'Assassina')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Tico', 'Liro')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguin('Tux', 'Imperial')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # O Tux cumprimentou swiiiin /// Method Resolution order - MRO


# Sabendo se é ou não instância de determinada classe ==================================================================

print(f'Tux é instância de Pinguin? -> {isinstance(tux, Pinguin)}')  # True
print(f'Tux é instância de Terrestre? -> {isinstance(tux, Terrestre)}')  # True
print(f'Tux é instância de Aquatico? -> {isinstance(tux, Aquatico)}')  # True
print(f'Tux é instância de object? -> {isinstance(tux, object)}')  # True
print(f'Tatu é instância de Aquatico? -> {isinstance(tatu, Aquatico)}')  # False
