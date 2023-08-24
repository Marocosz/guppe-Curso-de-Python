"""
Teste de memória dos Generators

# Sequência de Fibonacci:
1, 1, 2, 3, 5, 8, 13...


"""

# Função que realiza a sequência Fibonacci =============================================================================


# Utilizando Lista = 470 Mb


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


#  for n in fib_lista(100000):
#     print(n)


# Utilizando Generator = 4,8 Mb


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(100000):
    print(n)


# Ou seja, utilizando geradores temos 94 vezes menos uso de memória local