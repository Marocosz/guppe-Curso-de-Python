"""
JSON e Pickle

Json -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, YouTube, Facebook) e terceiros (Nós
desenvolvedores)


# Usando o Módulo Json =================================================================================================

# Usamos esse módulo para converter objetos python para objetos json

import json


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


felix = Gato('Felix')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)
"""

# Integrando Json com Pickle ===========================================================================================

# Usamos esse módulo para podermos traduzir objetos python para objetos json e vice versa

# pip install jsonpickle

import jsonpickle


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


felix = Gato('Felix')

# Escrevendo um arquivo json ===========================================================================================

with open('felix.json', 'w') as arquivo:  # Criamos um arquivo json utilizando objetos do Python
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo um arquivo json ================================================================================================

with open('felix.json', 'r') as arquivo:  # Traduzimos o arquivo Json para os objetos Python
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)