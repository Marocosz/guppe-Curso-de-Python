def data(dia, mes, ano):
    if mes == 1:
        mes = 'janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 3:
        mes = 'março'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    elif mes == 12:
        mes = 'dezembro'

    return f'{dia} de {mes} de {ano}'

print(data(14, 12, 2003))