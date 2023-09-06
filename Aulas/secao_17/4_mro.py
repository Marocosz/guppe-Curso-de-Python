"""
Method Resolution Order - MRO - POO

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem de execução dos métodos, qual será executado primeiro

Em Python, a gente pode conferir a ordem de execução dos métodos (mro) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

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


class Pinguin(Aquatico, Terrestre):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)


tux = Pinguin('Tux', 'Imperial')
print(tux.cumprimentar())  # O Tux cumprimentou swiiiin  # class Pinguin(Aquatico, Terrestre):

# Há o método 'cumprimentar' nas classes 'Aquatico', 'Terrestre' e 'Animal'
# Por que a resposta vem da classe 'Aquatico'? Pois de acordo com o MRO, por ela ser empregada primeiro na ordem,
# temos ela como resposta principal

print(Pinguin.__mro__)  # Ordem de Execução
