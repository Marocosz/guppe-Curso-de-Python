"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chmar de qualquer coisa
desde que comece com '*', ele não é um parâmetro obrigatório

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

O parâmetros *args utilizado em uma função, coloca os valores extras informados como entrada em uma utpla,
lembrando que as tuplas são imutaveis


    # Exemplo de *args -----------------------------------------------------------------------------------------------


def soma(*args):
    return sum(args)


print(soma())
print(soma(1, 2))
print(soma(1, 2, 3))

    # Outro Exemplo ---------------------------------------------------------------------------------------------------


def verificando_info(*args):
    if 'Marcos' in args and 'Rodrigues' in args:
        return f'Bem vindo {args}'
    else:
        return 'Não sei quem é você'

print(verificando_info('Marcos', 'Rodrigues'))
print(verificando_info('Heloísa', 'Pinheiro'))
print(verificando_info('Marcos'))
print(verificando_info('Marcos', 'Oliveira'))
"""

    # Desempacotando --------------------------------------------------------------------------------------------------


def soma(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5]

# print(soma(numeros))  # Error

print(soma(*numeros))

# OBS: O '*' serve para informar o python que o dado é uma coleção, sendo assim, ele automaticamente
# desempacota a variável que é uma coleção, no caso, uma lista
