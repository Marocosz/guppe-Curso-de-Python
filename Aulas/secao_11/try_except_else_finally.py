"""
Try / except / else / finally

Dica de quando e onde tratar código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!


# Exemplo Else =========================================================================================================

# Else -> É executado apenas se não ocorrer o except (erro)

try:
    num = int(input('Informe um número: '))

except ValueError:
    print('Valor incorreto')

else:
    print(f'Você digitou: {num}')


# Exemplo Finally ======================================================================================================

try:
    num = int(input('Informe um número: '))

except ValueError:
    print('Você não digitou um valor válido')

else:
    print(f'Você digitou o número {num}')

finally:
    print('Executando o Finally')

# OBS: O bloco finally é SEMPRE executado, independente se houve ou não uma exceção

# O finally geralmente é utilizado para fechar ou desalocar recursos


# Exemplo complexo ERRADO ==============================================================================================


def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))

except ValueError:
    print('O valor precisa ser númerico')

try:
    num2 = int(input('Informe o segundo número: '))

except ValueError:
    print('O valor precisa ser númerico')

try:
    print(dividir(num1, num2))

except NameError:
    print('Erro de declaração')


# Exemplo complexo CORRETO =============================================================================================

# OBS: Você é responsavel pelas entradas das suas funções, então, trate-as


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Impossivel dividir algum número por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Outro Exemplo ========================================================================================================


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError, ValueError) as erro:
        return f'Ocorreu o erro: {erro}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""

