"""
Herança (Inheritence) - POO

A ideia de Herança é a de reaproveitar código, mas também extender nossas classes

OBS: Com a Herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar
atributos e métodos da classe herdada

Cliente
    - Nome
    - Sobrenome
    - Cpf
    - Renda

Funcionário
    - Nome
    - Sobrenome
    - Cpf
    - Cargo


Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a
outras entidades?

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada

Quando uma Classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma Classe herda de outra classe, a classe que herda é conhecida por:
    [Cliente, Funcionario]
    - Sub Classe
    - Classe Filha
    - Classe Específica


Sobrescrita de método - Overriding

- Ocorre quando reescrevemos/reimplementamos um método presente na super classe dentro das classes filhas


OBS: Para acessarmos atributos privados fora de sua própria classe, usamos: self._Classe__atributo
por exemplo: self._Pessoa__nome


"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Colocamos na frente do class entre parentese o nome da classe que queremos herdar, por ex: 'class Cliente(Pessoa):'
# Utilizando o 'super()', temos acesso ao método construtor da Super Classe (Pessoa)


# Cliente 'Herda' de 'Pessoa'
class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


# Funcionário 'Herda' de 'Pessoa'
class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, cargo):
        super().__init__(nome, sobrenome, cpf)
        self.__cargo = cargo

    # Sobrescrita de Métodos
    def nome_completo(self):
        print(super().nome_completo())  # Dessa forma, conseguimos acessar o método da super classe
        return f'Nome: {self._Pessoa__nome} {self._Pessoa__sobrenome}  Cargo: {self.__cargo}'


c1 = Cliente('Marcos', 'Rodrigues', 15807167686, 5000)

f1 = Funcionario('Roberto', 'Guimarães', 12345612345, 'Atendente')

print(c1.nome_completo())
print(f1.nome_completo())

print(c1.__dict__)  # No dict de um objeto onde há classes herdadas na classe, terá todos os elementos de
                    # todas as classes
print(f1.__dict__)

