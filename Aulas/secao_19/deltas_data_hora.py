"""
Manipulando Deltas de Data e Hora

Delta = diferença entre uma coisa e outra coisa

data_incial = dd/mm/yyyy 12:55
data_final = dd/mm/yyyy  14:05
delta = data_final - data_inicial


# Diferença entre datas ================================================================================================

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2022, 11, 5, 16, 30)

tempo_para_evento = aniversario - data_hoje

print(tempo_para_evento)
print(tempo_para_evento.days)
print(tempo_para_evento.seconds)
print(repr(tempo_para_evento))


"""

# Somando na data ======================================================================================================

import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)  # timedelta = 3 dias, não terceiro dia ou algo assim, é um valor, 3 dias
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)

# Ou seja, 'vencimento_boleto' será igual a 'data_da_compra' + 3 dias
