"""
 Faça uma função chamada DesenhalLinha. Ele deve desenhar uma linha na tela usando
varios simbolos de igual (Ex: ========). A função recebe por parámetro quantos sinais
de igual serão mostrados.
"""


num = int(input('Qual a quantidade de "=" você quer?'))


def desenha_linha(mult):
    a = '=' * mult
    return a


print(desenha_linha(num))