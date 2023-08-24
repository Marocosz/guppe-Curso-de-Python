"""
Propriedades (Properties) - POO

Como recomendado, sempre utilizamos atributos privados, e com isso, a melhor forma de termos acesso ao valores
desses atributos privados, utilizamos métodos, chamados 'getters' para termos o acesso dos valores dos
atributos privados da classe, e os 'setters' para mudar valor de determinados atributos

Porém, em Python utilizamos o decorador '@property' no método, que tem a mesma função do 'getter'
ele é um método, porém para chamar ele, chamamos igual atributos

Para utilizarmos os 'setters' em Python, utilizamos o decorador '@atributo.setter' no método, por exemplo:

@limite.setter
def limite(self, novo_limite):
    self.__limite = novo_limite

chamar métodos = objeto.metodo()
chamar atributo = objeto.atributo   # Sem os '()'
chamar property = objeto.property   # Sem os '()' também

OBS: Tratamos o @property e o @atributo.setter da mesma forma como tratamos um atributo, porém são métodos propriedades


"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo: {self.__saldo}  cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Métodos 'Get' ====================================================================================================

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    # Métodos 'Set' ====================================================================================================

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite

    # Utilizando Propriedades ==========================================================================================

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Utilizando Setter em Python ======================================================================================

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    # ==================================================================================================================

    # Dessa forma, criamos meio que um atributo em forma de método

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Marcos', 3000, 5000)
conta2 = Conta('Helo', 20200, 10000)

print(conta1.extrato())
print(conta2.extrato())


# Chamamos a propriedade 'saldo' das duas contas e fizemos a soma
# OBS: Estamos fazendo acesso ao método saldo que é uma propriedade (@property), não ao atributo saldo, pois é privado
soma = conta1.saldo + conta2.saldo
print(soma)

# Chamando o setter
conta1.limite = 1233

print(conta1.__dict__)
print(conta1.valor_total)
