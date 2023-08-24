"""
Lambdas

São funções sem nome, ou seja, funções anônimas

# Função ===============================================================================================================

def funcao(x):
    return 3 * x + 1


print(funcao(10))

# Lambda sem entrada ===================================================================================================

amar = lambda: 'Eu amo python'

print(amar())

# Expressão Lambda =====================================================================================================

calc = lambda x: 3 * x + 1

print(calc(5))

# Lambda com múltiplas entrdas =========================================================================================

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('mARcos  ', '  rodriguEs   '))

# Exemplo ==============================================================================================================

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card'
           , 'Douglas Admas', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

# Com isso, ordenamos a lista de acordo com o sobrenome dos autores, utilizando o [-1] para pegar o último elemento
# e ordenar com o .sort em ordem alfabética

print(autores)
"""
# Funçaõ Quadratica ====================================================================================================


def quadr(a, b, c ):
    return lambda x: a * x ** 2 + b * x + c

teste = quadr(1, 2, 3)

print(teste(0))
print(teste(2))
print(teste(5))
print(quadr(2, 5, 9)(2))  # Sendo que os primeiros () são os parâmetros
                          # da função e os segundos () são os parâmetros do lambda




