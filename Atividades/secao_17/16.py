class Moto:

    def __init__(self, marca, modelo, cor, maior_marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__maior_marcha = maior_marcha
        self.__marcha = 0
        self.__ligada = False

    def imprimir(self):
        print(f'\nMarca: {self.__marca}\n'
              f'Modelo: {self.__modelo}\n'
              f'Cor: {self.__cor}\n'
              f'Maior Marcha: {self.__maior_marcha}\n'
              f'Marcha Atual: {self.__marcha}\n'
              f'Ligada: {self.__ligada}\n')

    def marchaAcima(self):
        if self.__ligada:
            if self.__marcha < self.__maior_marcha:
                self.__marcha += 1
                print(f'Você trocou para a marcha {self.__marcha}.')
            else:
                print('Você já está no limite mais alto da marcha')
        else:
            print('Ligue a Moto primeiro para poder mudar de Marcha')

    def marchaAbaixo(self):
        if self.__ligada:
            if self.__marcha > 0:
                self.__marcha -= 1
                print(f'Você trocou para a marcha {self.__marcha}.')
            else:
                print('Você já está no limite mais baixo da marcha')
        else:
            print('Ligue a Moto primeiro para poder mudar de Marcha')

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
            print('Você ligou a moto')
        else:
            print('A mota já está ligada')

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
            print('Você desligou a moto')
        else:
            print('A mota já está desligada')


moto1 = Moto('Fiat', 'xb22', 'Branca', 6)

moto1.imprimir()
moto1.ligar()
moto1.marchaAcima()
moto1.marchaAcima()
moto1.marchaAcima()
moto1.imprimir()
moto1.desligar()
moto1.imprimir()