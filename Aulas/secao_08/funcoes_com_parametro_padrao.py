"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional

    # Exemplo de função com parâmetro obrigatório ----------------------------------------------------------------------

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  # Deu Erro pois o parâmetro dessa função é obrigatório

    # Exemplo de função com parâmetro opicional -----------------------------------------------------------------------

def exponecial(numero, potencia=2):  # Adicionando o '=2' na frente do parâmetro, ele torna opicional, pois, se não
    return numero ** potencia        # houver no argumento, ele será definido como 2


print(exponecial(2, 3))
print(exponecial(2))

    # ERRO!!! -----------------------------------------------------------------------------------------------------

def teste(num=2, potencia):  # Está errado, pois, se houver apenas 1 valor com padrão ele deverá ficar
    return num * potencia    # apos os parametros sem padrão na declaração

    # Outro Exemplo --------------------------------------------------------------------------------------------------

def mostra_info(nome='Marcos', instrutor=False):
    if nome == 'Marcos' and instrutor == True:
        return 'Bem vindo Marcos'
    elif nome == 'Marcos':
        return 'Pensei que você era o Instrutor'
    elif nome != 'Marcos' and instrutor == True:
        return 'Ei! Você não é Instrutor(a)'
    else:
        return f'Olá {nome}'


print(mostra_info('Marcos', True))
print(mostra_info('Marcos'))
print(mostra_info('Heloísa', True))
print(mostra_info('Heloísa'))
print(mostra_info())x
print(mostra_info(instrutor=True))  # print(mostra_info(True))   dará True a variavel nome

    # Também podemos usar outras funções como parâmetro ---------------------------------------------------------------

def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(3, 3))
print(mat(3, 2, sub))

    # Escopo - Evitar problemas --------------------------------------------------------------------------------------

# Variáveis Globais
# Variáveis Locais

instrutor = 'Marcos'  # Variável Global

def diz_oi():
    instrutor = 'Rodrigues'  # Váriavel Local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Váriaveis locais tem preferência

def diz_oi():
    nome = 'Rodrigues'  # Váriavel Local
    return f'Oi {nome}'

print(diz_oi())
print(nome)  # Dá erro, já que a variável é local e esse comando não está dentro do bloco da variável

    # Erro de variável global ----------------------------------------------------------------------------------------

total = 0

def incremento():
    total = total + 1  # Tentar fazer operações com uma váriavel global com ela mesma, gera erro!
    return total


# Correto:

total1 = 0

def incremento1():
    global total1  # Dessa forma dizemos para o bloco que vamos utilizar a variável global
    total1 = total1 + 1
    return total1

print(incremento1())

    # Utiizando funções dentro de funções -----------------------------------------------------------------------------

def fora():
    contador = 1

    def dentro():
        nonlocal contador  # Ser 'nonlocal' siginfica ser uma váriavel não local e nem global, ou seja, local da função anterior

        contador = contador +1
        return contador
    return dentro()

print(fora())

"""