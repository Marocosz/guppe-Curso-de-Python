"""
Métodos Mágicos - POO

Métodos Mágicos, são todos os métodos que utilizam dunder.

Dunder -> Double Underscore

Método __repr__ -> Representação do objeto, quando pedimos para vermos determinado objeto: print(livro1) por exemplo

Método __str__ -> Igual o __repr__, porém com preferência, se existirem os dois, __str__ será utilizado, e pode ser
chamado apenas pelo - print(objeto)

Método __len__ -> Definimos oque aparecerá quando utilizarmos o método len no objeto da classe, sendo um número inteiro


# Podemos alterar todos os métodos mágicos nas nossas classes como logo abaixo, sempre tendo como base a teoria deles
# fazendo com que eles tenham uma função que nós determinarmos
"""


class Livro:

    def __init__(self, titulo, autor, pag):
        self.__titulo = titulo
        self.__autor = autor
        self.__pag = pag

    def __repr__(self):  # É muito utilizado para sabermos melhor como é determinado objeto
        return f'{self.__titulo} escrito por {self.__autor} de {self.__pag} páginas'

    def __str__(self):
        return f'{self.__titulo}'

    def __len__(self):
        return self.__pag

    def __add__(self, outro):
        return f'{self.__pag + outro.__pag}'

    def __mul__(self, outro):
        if int(outro):
            return self.__pag * outro
        else:
            return f'O valor precisa ser inteiro'

    def a(self):
        print('aaaaaaaa')


livro1 = Livro('Python Rocks', 'Marcos', 400)
livro2 = Livro('Inteli Py', 'Helo', 300)

print(repr(livro1))
print(str(livro1))
print(len(livro1))

print(livro1 + livro2)

print(livro1 * 2)

print(repr(Livro.a))