"""
Por que testar nosso código?
    - Reduzir bugs no código
    - Garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos
    - Garantem que bugs corrigidos anteriormente, continuam corrigidos
    - Garantem que a refatoração que costumamos fazer não tragam novos bugs

TDD -> Teste Driven Development (Desenvolvimento Guiado Por Testes)

Com TDD, é utilizado estágios de desenvolvimento:
    - Começa pelo teste
    - Escreve o código mínimo, suficiente para fazer o teste passar
    - Então, refatora o código para realizar a funcionalidade, e testa novamente
    - Visto que o teste passe, está finalizado

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red  # Criar o teste
    - Green  # Criar um código que passe no teste
    - Refactor  # Melhorar o código de acordo com oque precisa


Testes Automatizados
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.nome} mia...')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
