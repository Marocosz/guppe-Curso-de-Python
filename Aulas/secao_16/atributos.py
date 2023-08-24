"""
Atributos da POO

    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto, por exemplo, uma lâmpada, possivelmente iríamos querer saber se a
    lâmpada é 110 ou 220v, se ela é branca, amarela ou outra cor, qual é a luminosidade etc... Isso são os atributos

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos


# Atributos de Instância São atributos declarados dentro do método construtor

OBS: Método Construtor: É um método especial utilizado para a construção do objeto

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público, ou seja, pode ser acessado
em todo o projeto

Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da própria classe onde está declarado, utilizamos __ 'duplo underscore' no ínicio
do seu nome, também conhecido como Name Mangling


# Atributos de Instância Público =======================================================================================


class Lampada:

    def __init__(self, voltagem, cor):   # def __init__   -> Seria o Método Construtor
        self.voltagem = voltagem    # O self seria o objeto que está executando o método
        self.cor = cor
        self.ligada = False


class ContaCorrete:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos de Instância Privada =======================================================================================

# Atributos de Instância significa que ao criarmos instâncias/objeto de uma classe, todas as instâncias
# terão esses atributos especificados pela própria instância

class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Publico
        self.__senha = senha  # Privado

    def mostra_senha(self):
        print(self.__senha)  # Dessa forma podemos acessar o atributo privado tranquilamente, pois está dentro da class


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos
# atributos sinalizados como privados, fora da classe

# Exemplo:

user = Acesso('user@gmail.com', '12355')  # Criamos um objeto da classe 'Acesso' com os dois atributos

print(user.email)  # user@gmail.com  -  Atributo Público

# print(user.__senha)  # Error  -  Como é um atributo privado, não podemos acessa-lo dessa forma

# print(user._Acesso__senha)  # Temos acesso, porém não deveríamos. (Named Mangling)

user.mostra_senha()  # Como temos um método de mostrar a senha, podemos fazer dessa forma

# ======================================================================================================================

user1 = Acesso('user1@gmail.com', '12345')
user2 = Acesso('user2@gmail.com', '54321')

print(user1.email)
print(user2.email)


# Atributos de Classe ==================================================================================================


# class Produto:

#    def __init__(self, nome, descricao, valor):
#        self.nome = nome
#        self.descricao = descricao
#        self.valor = valor


# p1 = Produto('Playstation', 'Video Game', 2300)
# p2 = Produto('Xbox S', 'Video Game', 4500)


# Atributos de classe, são atributos, que são declarados diretamente na classe, ou seja, fora do construtor.
# Geralmente já inicialiszamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao
# invês de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos
# de classe, todas as instâncias terão o mesmo valor para determinado atributo

# Refatorando o class 'Produto':


class Produto:

    imposto = 1.05  # Atributo de classe - 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 3000)

print(p1.imposto)
print(p2.imposto)

print(p1.valor)
print(p2.valor)

print(p1.id)
print(p2.id)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso aos 'Atributos de Classe'

print(Produto.imposto)  # Podemos acessar dessa maneira
"""

# Atributo Dinâmico ====================================================================================================

# OBS: O Atributo Dinâmico será exclusivo da instância que o criou


class Produto:

    imposto = 1.05  # Atributo de classe - 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Arroz', 'Alimento', 5.99)
p2 = Produto('Feijão', 'Alimento', 2.50)

p2.peso = '5kg'  # Esse seria o atributo dinâmico, observe-se que não existe na class Produto

print(p2.peso)  # Ele pode ser 'chamado' apenas pelo produto 'p2', pois é específico dele


# Deletando atributos ==================================================================================================

print(p2.__dict__)  # Vemos todos os atributos da instância

del p2.peso  # Dessa forma deletamos o atributo

print(p2.__dict__)

# Podemos remover atributos independentes se são de Instância, de Classe ou de Dinãmicos
