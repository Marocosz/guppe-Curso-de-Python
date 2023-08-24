"""
Funções de Matemáticas e Estatísticas


# math.prod ============================================================================================================

# Retorna o produto de um container numérico

import math

nuns_v1: list = [2, 3, 6, 8]
nuns_v2: tuple = (2, 3, 6, 8)
nuns_v3: set = {2, 3, 6, 8}

print(math.prod(nuns_v1))  # 2 * 3 * 6 *8 = 288
print(math.prod(nuns_v2))  # 288
print(math.prod(nuns_v3))  # 288


# math.isqrt ===========================================================================================================

# Retorna o inteiro da raiz quadrada de um número

import math

print(math.isqrt(9))  # 3
print(math.isqrt(25))  # 5
print(math.isqrt(17))  # 4

print(math.sqrt(9))  # 3.0 - Retorna todo o número da raiz quadrada de um número
print(math.sqrt(17))  # 4.123105625617661


# math.dist ============================================================================================================

# Retorna a distância euclidiana entre pontos 3d ou 2d

import math

# 3d:

p3d1 = [12, 50, 34]
p3d2 = [23, 2, 98]

# 2d:

p2d1 = [2, 6]
p2d2 = [6, 12]

print(math.dist(p3d1, p3d2))  # 80.75270893288967
print(math.dist(p2d1, p2d2))  # 7.211102550927978


# math.hypot ===========================================================================================================

# Retorna a hipotenusa

import math

nums = [3, 4, 5]
print(*nums)  # 3 4 5

print(math.hypot(*nums))  # '*' para descompactar a lista 'nums' - 7.0710678118654755
print(math.hypot(12, 53, 10))  # 55.25395913416522


# Estatísticas =========================================================================================================

# statistics.fmean =====================================================================================================

# Calcula a média de números reais

import statistics

valores_reais = [1.45, 7.34, 23.321, 256.23]
valores_int = [1, 56, 2, 3, 12]

print(statistics.fmean(valores_reais))  # 72.08525
print(statistics.fmean(valores_int))  # 14.8


# statistics.geometric_mean ============================================================================================

# Calcula a média de números reais

import statistics

valores_reais = [1.45, 7.34, 23.321, 256.23]
valores_int = [1, 56, 2, 3, 12]

print(statistics.geometric_mean(valores_reais))  # 15.880358481622313
print(statistics.geometric_mean(valores_int))  # 5.2614337305174175
"""

# statistics.multimode =================================================================================================

# retorna o valor mais frequente de uma sequência

import statistics

seq1 = 'Marcos Rodrigues'
seq2 = [1, 2, 6, 4, 2, 2, 5, 6, 10, 2, 4, 4, 3, 5]

print(statistics.multimode(seq1))  # ['r', 'o', 's']
print(statistics.multimode(seq2))  # [2]