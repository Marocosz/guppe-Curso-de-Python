class Robo:

    def __init__(self, nome, bateria=100, habildiades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habildiades


    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Beep, beep, sou o {self.__nome}, o robo!'
        return 'Sem bateria!'

    def aprender(self, habilidade_nova, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(habilidade_nova)
            return f'Uau, aprendi {habilidade_nova}'
        return 'Sem bateria para aprender essa habilidade'

    