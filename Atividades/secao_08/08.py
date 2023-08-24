import math


def catetos(a, b):
    t = math.isqrt((a**2) + (b**2))
    return f'A hipotenusa do triangulo com esses catetos é {t}'


print(catetos(5, 6))