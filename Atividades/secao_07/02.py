valor = input('Digite seis números inteiros, os separando com vírgula')


valor1 = valor.split(',')
len(valor1)

for x in valor1:
    if x == ' ':
        valor1.remove(x)

cont = 0

while len(valor1) == 6 and cont == 0:
    print(valor1)
    cont = 1
else:
    if cont != 1:
        print('Digite 6 númeors inteiros')

