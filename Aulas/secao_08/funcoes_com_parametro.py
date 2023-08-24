"""
Funções com Parâmetro (De Entrada)

Parâmetros -> Parâmetros são a parte da variável que define a função
Argumentos -> São os dados passados para subistituir os parâmetros na execução da função

OBS: A ordem dos parâmetros e argumentos são importantes


- Funções que recebem dado para serem porcessados dentro da mesma

Se a gente pensar em algum programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em funções, já sabemos que:
- Não possuem entrada
- Não possuem saída
- Possuem entrada mas não possuem saída
- Não possuem entrada mas possuem saída
- Posseum entrada e saída

    # Função com parâmetro com return  --------------------------------------------------------------------------------
def quadrado(numero):
    return numero * numero


print(quadrado(7))
print(quadrado(6))
print(quadrado(3))

print(quadrado())  # Vai dar erro devido a falta do parâmetro que é obrigatório

    # Outra função com parâmetro sem return ---------------------------------------------------------------------------

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens('Marcos')

# OBS: Função podem ter N parâmetros de entrada, ou seja, ilimitado e se houver mais de 1 tem que separar por vírgula

    # Função com mais de um parâmetro --------------------------------------------------------------------------------

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def outra(num1, num2, msg):
    return (num1 + num2) * msg


print(soma(2, 3))
print(soma(5, 2))

print(multiplicacao(13, 2))
print(multiplicacao(3, 6))

print(outra(10, 2, 'Oi'))
print(outra(2, 3, 'Essa não '))

# OBS: Se informaar um número errado de parâmetro/argumento terá um erro

print(soma(1, 3, 4))  # Erro por passar argumentos a mais
print(soma(1))  # Erro por passar argumento a menos
print(soma(a, b))  # Erro por passar tipo de argumento diferente do que a função exige

    # Nomeando parâmetros ------------------------------------------------------------------------------------------

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Marcos', 'Rodrigues'))

# OBS: É importante sempre nomear os parâmetros de acordo com a função desejada para melhor visualização

    # Argumentos nomeados (Keywords Arguments) -------------------------------------------------------------------------

# Caso utilizemos nomes dos parâmetros nos argumentos, podemos utilizar qualquer ordem

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo(sobrenome= 'Rodrigues', nome = 'Marcos'))

nome = 'Marcos'
sobrenome = 'Rodrigues'

print(nome_completo(sobrenome = sobrenome, nome = nome))

    # Erro comum na utilização do return ------------------------------------------------------------------------------

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

print(soma_impares([1, 2, 3, 4]))

# Lembre-se sempre que o return finaliza a função, sendo assim, se estiver dentro de um loop, o loop acabará.
"""


def multiplicacao(a, b):
    return a * b
