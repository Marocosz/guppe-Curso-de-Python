"""
Doctests

Doctest -> É um teste dentro da documentação de uma função

# Para ver usamos: python -m doctest -v Aulas.secao_20.doctests.py
# dentro do terminal, ai teremos a descrição dos testes

OBS: Se o resultado não for exatemente igual deverá aparecer no prompt, irá calcular como errado
"""


def soma(a, b):
    """Somam os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b
