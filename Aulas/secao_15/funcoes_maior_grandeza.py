"""
Funções de maior grandeza - Higher Order Functions - HOF


- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado, ou que podemos passar funções como argumento de outras funções, e até mesm ocriar variáveis do tipo
funções nos nossos programas


# Exemplos - Definindo as funções ======================================================================================


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(num1, num2, funcao):
    return funcao(num1, num2)


print(calc(2, 3, mult))
print(calc(5, 2, somar))
print(calc(10, 2, div))

# Dessa forma vemos que utilizamos outras funções dentro do argumento de uma função, porém temos que prestar atenção
# no método que está escrito o bloco da função que pegará outra função como arg


# Nested Functions - Funções aninhadas =================================================================================

# Em python, podemos ter funções dentro de funções - Inner Functions (Funções internas)

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí', 'Suma daqui!', 'Gosto muito de você', 'Olá'))
    return humor() + ' ' + pessoa


print(cumprimento('Marcos'))
print(cumprimento('Marcos'))
print(cumprimento('Marcos'))


# Retornando Funções de outras funções =================================================================================

from random import choice


def faz_me_rir():
    def rir():
        return choice(('HAHAHAHAHAHAHA', 'KKKKKKKKKKKKKKKKKKKKKK', 'JAJAJAJJAJAJAJJAJAJAJJA'))

    return rir  # Não Retornando a função 'rir'


# Quando utilizamos a função com '()' estamos retornando ela, quando não utilizamos '()' apenas estamos rodando a
# função, sem retorna-la

print(faz_me_rir())  # Retornando apenas a função 'faz_me_rir'
print(faz_me_rir()())  # Retornando as duas funções, a 'faz_me_rir' e a 'rir' que está interna
print(faz_me_rir)  # Não retornando nenhuma função

# Porém, pra não precisarmos retornar as duas funções dessa forma, podemos retornar a função diretamente por dentro
# da função utilizando o '()' mesmo


# Inner functions podem acessar o escopo de funções mais externas =====================================================

from random import choice


def rindo(pessoa):
    def risada():
        r = choice(('HAHAHAHA', 'HEHEHEHEH', 'Kkkkkkkkkkkkkkkkk'))
        return f'{r}, {pessoa}'

    return risada()


print(rindo('Marcos'))

# Ou seja, podemos utilizar as variáveis ou até mesmo o argumento das funções externas


# Sobre retornar funções ===============================================================================================


def func():
    print('Olá')
    return 'Não olá'


func()  # Dessa forma, estará apenas rodando a função, ou seja, irá apenas fazer oque está
        # no bloco, no caso, printar 'Olá'

func  # dessa forma nada irá ocorrer

print(func())  # dessa forma, a função rodará e também retornará seu return, mostrando o return e o print

print(func)  # Dessa forma teremos apenas <function func at 0x0000020CD8783E20>


# Função dentro de função ==============================================================================================

def oi():
    def ola():
        print('olá')
        return 'Olááá'
    print('oi')
    return ola


oi()  # Vai apenas rodar a função, no caso, printar 'oi'

oi()()  # Vai rodar as duas funções, no caso, printar 'oi' e 'olá'

print(oi())  # Dessa forma vai apenas rodar a função oi e
print(oi()())  # Dessa forma vai rodar e retornar as duas funções
"""




