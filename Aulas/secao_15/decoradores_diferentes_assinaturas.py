"""
Decorators com diferentes assinaturas


# Exemplo com problema =================================================================================================


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Eu gostaria de {principal} com {acompanhamento}'


print(saudacao('Marcos'))  # Correto
print(ordenar('Picanha', 'Molho'))  # Errado, pois a função 'aumentar' recebe apenas 1 argumento e a 'ordenar' recebe 2



# Resolvendo o problema acima ==========================================================================================


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, sou o {nome}'


@gritar
def ordenar(principal, acompanhamento, molho = 'Ketchup'):
    return f'Eu gostaria de {principal} com {acompanhamento}'


print(saudacao('Marcos'))  # Correto
print(ordenar('Picanha', 'Batata Frita'))  # Correto

# Corrigimos o problema utilizando args e kwargs, assim, não importanto a quantidade de argumentos/parametros
# necessarios para as funções, e não importa o argumento/parametro que seja dado na função, pode ser com parâmetros
# padrão, ou não
"""


# Decorators com parâmetros ============================================================================================


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args[0] != valor:
                return f'O valor está incorreto, o primeiro argumenta precisar ser {valor}'
            else:
                return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(2)
def soma(num1, num2, num3):
    return num1 + num2 + num3


print(soma(10, 2, 3))  # O valor está incorreto, o primeiro argumenta precisar ser 10
print(comida_favorita('Arroz', 'Salada', 'Feijão'))  # O valor está incorreto, o primeiro argumenta precisar ser Pizza

# Dessa forma podemos dar parâmetro para a decorator, que pega esse parâmetro incluso na assinatura para rodar seu bloco
# Que no caso, acontece da seguinte forma: temos a primeira função que receberá algum argumento, e dentro do seu bloco
# haverá outra função que receberá a função que será decorada, e então no seu bloco haverá outra função com o real
# código que queira, no caso, esse código analisa se o primeiro argumento é diferente do parâmetro da primeira função
# e se for fará 'x' coisa, e para darmos o argumento que a primeira função necessita, o passamos na assinatura do '@'
''