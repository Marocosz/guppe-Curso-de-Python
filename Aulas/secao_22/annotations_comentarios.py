"""
Annotations nos comentários


"""

# Exemplo ==============================================================================================================

import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f'{texto} com alinhamento'
    else:
        return f'{texto} sem alinhamento'


nome = 'Marcos'  # type: str


# dessa forma, o mypy também funciona, porém, recomendo usar dentro da própria função, em vez de usar nos comentários
