class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def printar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Altura: {self.altura}')

    def sets(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


pessoa1 = Pessoa('Marcos', 18, 1.80)

pessoa1.printar()

