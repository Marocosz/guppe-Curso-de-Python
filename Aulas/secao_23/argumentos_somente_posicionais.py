"""
Argumentos somente posicionais
"""

# Testando =============================================================================================================


def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('Marcos'))  # Olá Marcos
print(cumprimenta_v1(nome='Marcos'))  # Olá Marcos


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('Marcos'))  # Olá Marcos
# print(cumprimenta_v2(nome='Marcos'))  # Error - Função com argumento posicional


def cumprimentar_v3(nome, sobrenome, /, mensagem='Olá'):
    return f'{mensagem} {nome} {sobrenome}'


print(cumprimentar_v3('Marcos', 'Rodrigues', mensagem='Oi'))  # Oi Marcos Rodrigues
print(cumprimentar_v3('Marcos', 'Rodrigues'))  # Olá Marcos Rodrigues
# print(cumprimentar_v3(nome = 'Marcos', sobrenome='Rodrigues', 'hello'))  # Error


# OBS: Ou seja, todos os parâmetros anterior a '/' são argumentos posicionais


# O Contrário ==========================================================================================================


def cumprimentar_v4(*, nome):
    return f'Olá {nome}'


print(cumprimentar_v4(nome='Marcos'))  # Olá Marcos
# print(cumprimentar_v4('Marcos'))  # Error


# OBS: O Contrário da '/', todos os parâmetros depois do '*' são apenas parâmetros nomeados, como no exemplo


# Usando tudo ==========================================================================================================


def cumprimentar_v5(nome, /, mensagem1='Ola', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v5('Marcos', 'Eai', mensagem2='Tudo bem?'))  # Eai Marcos Tudo bem?
print(cumprimentar_v5('Marcos', mensagem1='Coé', mensagem2='Joia?'))  # Coé Marcos Joia?
# print(cumprimentar_v5(nome='Marcos', 'Opa', 'Blz?'))  # Error
