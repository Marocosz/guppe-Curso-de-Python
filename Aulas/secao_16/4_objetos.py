"""
Objetos da POO

Objetos -> São instâncias da Classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma
classe como variáveis do tipo definido na Classe, com as características pré descritas pela classe

# OBS: O 'self' dos parâmetros das funções da classe é a representação do próprio objeto/instância

# OBS: Podemos criar métodos com parâmetros padrão, lembrando que os parâmetros padrões devem sempre ficar ao final


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            print(f'{self} já está ligada!')

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            print(f'{self} já etá desligada!')


class Cliente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é: {self.__cliente.nome}')  # Utilizando a Classe 'Cliente' dentro da classe 'ContaCorrente'
        print(f'O seu cpf é: {self.__cliente.cpf}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Objetos ==============================================================================================================

# São feitos da forma abaixo, sempre determinando os parâmetros que a classe pede

lamp1 = Lampada('Branca', 110, 60)  # Instância da classe 'Lampada'

print(lamp1.checa_lampada())

lamp1.ligar()

print(lamp1.checa_lampada())

user1 = Usuario('Marcos', 'Rodrigues', 'marcosrodrigues@gmail.com', '159951')  # Instância da classe 'Usuario'


# Usando Objetos como Argumentos =======================================================================================

cl2 = Cliente('Marcos', 15807167686)

cc2 = ContaCorrente(5000, 10000, cl2)  # Usamos como o terceiro argumento o objeto 'cl2' da classe 'Cliente'

cc2.mostra_cliente()

print(help(Usuario))