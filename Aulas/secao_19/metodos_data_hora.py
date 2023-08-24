"""
Métodos de Data e Hora


# now e today ==========================================================================================================

import datetime

agora = datetime.datetime.now()
print(agora)  # 2022-05-17 18:01:59.301737
print(repr(agora))  # datetime.datetime(2022, 5, 17, 18, 1, 59, 301737)

hoje = datetime.datetime.today()
print(hoje)  # 2022-05-17 18:01:59.301737
print(repr(hoje))  # datetime.datetime(2022, 5, 17, 18, 1, 59, 301737)

# Com 'now', podemos especificar um timezone (fuso horário)


# Mudanças à meia-noite ================================================================================================

import datetime

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(repr(manutencao))

# combine -> Serve para combinar duas funções do datetime
# now -> Serve para pegar a data/hora no momento que executado
# timedelta -> Serve para dar um valor em dias
# time -> Serve para definir as horas, por padrão é tudo 0


# Encontrando um dia da semana =========================================================================================

# Usamos o método 'weekday' para sabermos o dia da semana, e ele vai de 0 a 7, sendo 0 segunda, 1 terça....

import datetime

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())  # 2 - Quarta


# Iterando com weekday =================================================================================================

import datetime

nasc = input('Informe sua data de nascimento (dd/mm/yyyy): ')  # String

nasc = nasc.split('/')  # List

nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))

if nasc.weekday() == 0:
    print('Voce nasceu numa segunda-feira!')
elif nasc.weekday() ==1:
    print('Voce nasceu numa terça-feira!')
elif nasc.weekday() ==2:
    print('Voce nasceu numa quarta-feira!')
elif nasc.weekday() ==3:
    print('Voce nasceu numa quinta-feira!')
elif nasc.weekday() ==4:
    print('Voce nasceu numa sexta-feira!')
elif nasc.weekday() ==5:
    print('Voce nasceu num sábado!')
elif nasc.weekday() ==6:
    print('Voce nasceu num domingo!')


# Formatando datas/horas ===============================================================================================

# Usamos strftime() -> (String Format Time)

import datetime

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # Podemos alterar para 'y' minúsculo para termos dois algarismos no ano
print(hoje_formatado)                       # Temos o '%B' no lugar do mês para colocarmos o mês em palavra
                                            # E também podemos usar apenas um, por exemplo hoje.strftime('%B')


# Usando strptime =====================================================================================================

import datetime

# Usamos strptime para traduzir uma string numa data

nascimento = datetime.datetime.strptime('14/12/2003', '%d/%m/%Y')
print(nascimento) # 2003-12-14 00:00:00


# Usando apenas a Hora =================================================================================================

almoco = datetime.time(12, 30, 0)
print(almoco)  # 12:30:00


# Marcando tempo de execução do nosso código ===========================================================================

import timeit

# Recebe uma expressão em formato de string que será executada por baixo dos panos, e como segundo
# argumento, a quantidade de vezes que essa expressão será executada

# loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
print(tempo)  # 1.7470386000350118

# list comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
print(tempo)  # 1.4805018000188284

# map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100000)
print(tempo)  # 1.285072600003332
"""

# Usando Functools =====================================================================================================

import functools
import timeit


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num + n ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=1000))  # 0.6008181000361219 segundos

# functools.partial(funçao, parametro_da_função) -> Serve para executar determinada função
