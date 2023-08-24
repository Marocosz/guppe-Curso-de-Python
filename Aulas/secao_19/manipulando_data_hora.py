"""
Manipulando Data e Hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime


# Conhecendo Datetime ==================================================================================================

import datetime

# print(dir(dateetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Data e Hora Atual
print(datetime.datetime.now())  # 2022-05-17 11:15:21.682452
print(repr(datetime.datetime.now()))  # datetime.datetime(2022, 5, 17, 11, 16, 54, 388916)

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)
# Alterando as informações da data/hora
inicio = inicio.replace(hour=16, minute=0, second=2)
print(inicio)


# Criando datas ========================================================================================================

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(evento)
print(type(evento))

# Recebendo datas de usuário ===========================================================================================

nasc = input('Informe sua data de nascimento (dd/mm/yyyy): ')  # String

nasc = nasc.split('/')  # List

nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))

print(nasc)
print(type(nasc))


"""

# Acesso individual dos elementos ======================================================================================

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(evento.year)  # Ano
print(evento.day)  # Dia
print(evento.second)  # Segundo


# Formatando data ======================================================================================================

data_a = datetime.date.today()
data_atual = ('{d}'+'/' + '{m}' + '/' + '{y}').format(d=data_a.day, m=data_a.month, y=data_a.year)
print(data_atual)
data_atual_list = data_atual.split('/')
print(data_atual_list)