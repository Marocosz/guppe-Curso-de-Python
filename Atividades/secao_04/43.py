valor = float(input('Valor do produto:'))
a_vista = valor * 0.9
comissao1 = a_vista * 0.05
a_prazo = valor / 3
comissao2 = valor * 0.05

print(f'Pagando a vista o comprador deve pagar {a_vista} e a comissão será de {comissao1}')
print(f'Pagando a em parcelas de 3 meses, o comprador deve pagar {a_prazo} por mês, e a comissão será de {comissao2}')
