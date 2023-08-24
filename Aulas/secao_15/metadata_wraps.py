"""
Preservando Metadatas com Wraps

Metadatas -> São dados intrínsecos dentro do arquivo

Wraps -> São funções que envolvem elementos com diversas finalidades


# Problema =============================================================================================================


def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois números
    return a + b


# print(soma(1, 2))  # Normal

print(soma.__name__)  # logar
print(soma.__doc__)  # Eu sou uma função (logar) dentro de outra

# Ou seja, ao decorar uma função e pedir os seus metadados, o python dará os dados da função decoradora, assim, sendo
# um erro, o certo seria dar os metadados da própria função, e pra resolvermos isso, usamos o import wraps de functools
"""

# Resolução Problema ===================================================================================================

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Dessa forma os metadados da função será guardado devidamente
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(1, 2))  # Normal

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números

# Ou seja, ao decorar uma função e pedir os seus metadados, o python dará os dados da função decoradora, assim, sendo
# um erro, o certo seria dar os metadados da própria função, e pra resolvermos isso, usamos o import wraps de functools
