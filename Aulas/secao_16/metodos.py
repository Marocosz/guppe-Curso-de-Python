"""
Métodos da POO

    - Métodos (Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
    no seu sistema

    - Métodos são escritos em letras minúsculas e os nomes compostos, separados por '_'

Em Python, dividimos os métodos, em dois grupos: Métodos de Instância e Métodos de Classe

# O Método dunder init (__init__), e um método especial chamado construtor, e sua função é construir
  o objeto a partir da classe

OBS: Os métodos/funções dunder em Python, são chamados métodos mágicos

OBS: utilizamos 'self.ItemDoConstrutor' para referirmos ao próprio objeto da classe

ATENÇÂO: Por mais que possamos criar métodos/funções utilizando dunder, não é recomendável, pois é uma forma do
python diferenciar seus métodos builtins, sendo assim, pode ser que ao criar uma função com dunder, cause interferência

========================================================================================================================

nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
email = input('Informe seu email: ')
senha = input('Crie sua senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(1)  # Serve para terminar o programa

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(user.mostra_cryp())

========================================================================================================================
"""

# Classes ==============================================================================================================


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * ((100 - porcentagem) / 100)


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def mostra_cryp(self):
        return self.__senha


# Métodos de Instância =================================================================================================

# Usamos Métodos de Instância quando precisamos fazer acesso a Atributos de Instância, são formulados da forma comum
# De funções, usando apenas 'def', com a diferença do 'self'


# Métodos de Classe ====================================================================================================

# Usamos Métodos de Clase, quando precisamos fazer acesso de Atributos de Classe

# Para criar um Método de Classe, precisamos utilizar o decorador '@classmethod'
# E a forma correta de acesso, é via Nome da Classe, exemplo:

Usuario.conta_usuarios()  # Forma correta de acesso de um Método de Classe


# Métodos Privados =====================================================================================================

# Temos Métodos Privados, onde são métodos que apenas são acessados na Classe
# Para criarmos um Método Privado, adicionamos dunder no começo do seu nome, ex: def __checa_senha


#  Métodos Estáticos ===================================================================================================

# Bem parecido com os Métodos de Classe, com a diferença que utiliza-se o decorador '@staticmethod'
# Sua função é retornar valores não referentes a nada da Classe nem dos Objetos

