"""
Conhecendo o Pickle

A função do pickle é 'binarizar' um objeto Python e pode ocorrer o inverso

Este processo é chamado serialização/deserialização

# De modo geral, o pickle serve como uma forma mais segura de se guardar dados, pois binariza objetos python, impedindo
# de saberem oque há no arquivo

#OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos Pickle
vindo fontes desconhecidas


# Escrevendo em arquivo Pickle =========================================================================================

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)



"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo Leitura de arquivos Pickle ===================================================================================

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O Gato chama {gato.nome}')
    print(f'O Cachorro chama {cachorro.nome}')
    gato.mia()
    cachorro.late()
    print(type(gato))
    print(type(cachorro))
