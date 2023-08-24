"""
Documentando Funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função utilziando a propriedade .__doc__
"""

    # Criando uma Docstring -------------------------------------------------------------------------------------------

def diz_oi():
    """ Uma função simples que retorna a string 'oi!'."""
    return 'Oi!'


print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Número que será elevado ao exponencial, que, por padrão é 2
    :return: numero ** potencia
    """
    return numero * potencia

print(exponencial.__doc__)
