"""
Faça uma funçã0 que receba a distāncia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixO:
"""


def consumo(km, l):
    kml = km/l
    if kml < 8:
        return f'Venda o carro {kml}'
    elif 14 > kml > 8:
        return f'Econômico {kml}'
    elif kml > 14:
        return f'Super econômico {kml}'


print(consumo(100, 25))
print(consumo(60, 2))
print(consumo(100, 1))