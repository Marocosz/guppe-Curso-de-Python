"""
Geradpres

- Geradores (Generators) são iteradores (iterators)

OBS: O contrário não é verdadiero, nem todo iterator é um generator

Outras infos:
    - Generators podem ser criados com funções geradoras
    - Funções geradoras utilizam a palavra reservada yield
    - Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions:

Funções:                           || Generator Functions:
                                   ||
Utilizam return                    || Utilizam yield
Retorna apenas uma vez             || Pode usar yield múltiplas vezes
Quando executada, retorna um valor || Quando executada, retorna um generator

"""

# Exemplo Generator Function ===========================================================================================


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# OBS: Uma Generator Function não é um generaator, ela GERA um generator

gen = conta_ate(10)

print(type(gen))  # <class 'generator'>

print(next(gen))  # 1

print('-----')

for num in gen:
    print(num)  # 2...10

# O Yield serve como o return, porém não é finalizado quando entra nele, a cada next utilizado sobre a função
# teremos o retorno do yield novamente, assim até a ocorrer todos os next possiveis