"""
Teste de velocidade dos Generators Expression


# Generator ===========================================================================================================


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # <generator object nums at 0x00000256FE9B1D90>  # Generator

print(next(ge1))
print(next(ge1))

# Generator Expression =================================================================================================

ge2 = (num for num in range(1, 10))

print(ge2)  # <generator object <genexpr> at 0x000002787B699A10>  # Generator Expression

print(next(ge2))
print(next(ge2))
"""

# Realizando o teste de velocidade =====================================================================================

import time

# Generator Expression:

gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))  # 4999999950000000
gen_tempo = time.time() - gen_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(1, 100000000)]))  # 4999999950000000
list_tempo = time.time() - list_inicio

print(gen_tempo)  # 11.626515865325928
print(list_tempo)  # 16.9503390789032

# Ou seja, a velocidade de processamento do Generator Expression é menor que a velocidade da List Coprehenssion
