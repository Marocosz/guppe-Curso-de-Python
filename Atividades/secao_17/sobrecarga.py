
class Pessoa:

    codigo = 0

    def __init__(self):
        print('Construtor Padrão')
        nome = input('Digite o Nome da pessoa: ')
        idade = input('Digite a Idade da pessoa: ')
        id = Pessoa.codigo
        self.__nome = nome
        self.__idade = idade
        Pessoa.codigo += 1

    def exibe(self, var=1):
        if var == 1:
            print(f'Nome: {self.__nome}\n'
                  f'Idade: {self.__idade}\n')
        else:
            print(f'Nome: {self.__nome}\n')



pessoa1 = Pessoa()
pessoa1
pessoa1.exibe()
