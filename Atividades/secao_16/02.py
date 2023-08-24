class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


class Agenda:
    pessoas = []

    def __init__(self, nome, idade, altura):
        self.__pessoa = Pessoa(nome, idade, altura)
        if len(Agenda.pessoas) < 3:
            Agenda.pessoas.append((self.__pessoa.nome, self.__pessoa.idade, self.__pessoa.altura))
        else:
            print('Limite Máximo de Pessoas')

    @classmethod
    def lista_agenda(cls):
        if len(Agenda.pessoas) <= 3:
            for x in Agenda.pessoas:
                print(f'Nome: {x[0]}\nIdade: {x[1]}\nAltura: {x[2]}\n')
        else:
            print('Há mais de 3 pessoas adicionadas')

    @classmethod
    def busca_index(cls, nome):
        for x in Agenda.pessoas:
            if x[0] == nome:
                print(f'A posição deste contato é: {Agenda.pessoas.index(x) + 1}')

    @classmethod
    def busca_pessoa(cls, index):
        print(f'Nome: {cls.pessoas[index-1][0]}\nIdade: {cls.pessoas[index][1]}\nAltura: {cls.pessoas[index][2]}')

    @classmethod
    def remove(cls, nome):
        for x in cls.pessoas:
            if x[0] == nome:
                cls.pessoas.remove(x)


