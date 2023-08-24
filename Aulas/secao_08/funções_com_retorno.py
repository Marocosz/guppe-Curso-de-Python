"""
Funções com Retorno

A Vantagem de uma função com retorno é a possibilidade de operar a função, diferente se não tivesse retorno

OBS: Não precisamos necessárimente criar uma variável para retornar uma função, basta utilizar a função
OBS: Funções com retorno utiliza-se 'return'

numeros = [1, 2, 3, 4]

ret = numeros.pop()  # Há retorno

print(numeros)  # Não há retorno (None)

    # Exemplo Função Sem Retorno ------------------------------------------------------------------------------------

def quadrado_sete():
    print(7 * 7)


ret = quadrado_sete()

print(f'Retorno = {ret}')

    # Exemplo Função com Retorno -------------------------------------------------------------------------------------

def quadrado_sete():
    return 7 * 7        # Para retornar os valores usamos a palavra reservada 'return'

ret = quadrado_sete()

print(f'Retorno = {ret}')  # Retorno com variável
print(f'Retorno = {quadrado_sete()}')  # Retorno com a função

    # Refatorando a primeira função  ----------------------------------------------------------------------------------

def diz_oi():
    return 'Oi!'

print(diz_oi())

    # Exemplo 01   -----------------------------------------------------------------------------------------------------

OBS: 'return' finaliza a função

def diz_oi():
    print('estou sendo executado antes do retorno')
    return 'Oi!'
    print('Estou sendo executada depois do return')  # Não é executado já que está depois do return

print(diz_oi())

    # Exemplo 02  -----------------------------------------------------------------------------------------------------

    OBS: Podemos ter numa função, diferentes 'returns'

def nova_funcao():                # Com diferente returns
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'

print(nova_funcao())

    # Exemplo 03  -----------------------------------------------------------------------------------------------------

OBS: Podemos retornar qualquer tipo de dado e até mesmo múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(outra_funcao())

    # Vamos criar uma função para jogar moeda -------------------------------------------------------------------------

from random import random

def joga_moeda():
    # Gera um número pseudo randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'

print(joga_moeda())

"""

    # Erros Comuns  -------------------------------------------------------------------------------------------------

