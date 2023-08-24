"""
Abstração e Encapsulamento da POO

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes

Encapsulamento -> Agrupamento dos métodos e atributos da classe em objetos de forma com que as etapas aconteçam da
forma correta, sem alterações indesejáveis

Abstração -> É o ato de expor apenas dados relevantes de uma classe nos objetos para os usuários, ou seja, as
informações não relevantes para o usuário não são expostas para ele

"""

# ======================================================================================================================

class Conta:

    contador = 399

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} reais, do titular {self.titular} com limite de {self.limite} reais')

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        conta_destino.saldo += valor



conta1 = Conta('Marcos', 10000, 3000)

print(conta1.numero)
print(conta1.titular)
conta1.extrato()
conta1.depositar(1000)

conta1.numero = 12312
conta1.titular = 'Marcoswdssd'

# Ou seja, com os atributos públicos, podemos alterar os dados, assim, ignorando as etapas de modificação da própria
# classe, sendo assim, o melhor é sempre fazer os atributos privados, para evitar alterações indesejadas

# Quando os atributos da classe são públicos, não há o devido ENCAPSULAMENTO da classe

