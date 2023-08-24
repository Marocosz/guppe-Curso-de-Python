valor = input('Digite 10 números \n')

valor1 = valor.split(',')

for x in valor1:
    if x == ' ':
        valor1.remove(x)

cont = 0

while len(valor1) == 10 and cont == 0:
    cont = 1

if cont == 0 and len(valor1) != 10:
     print('Digite 6 númeors inteiros')

if cont == 1:
    i1 = int(valor1[0]) ** 2
    i2 = int(valor1[1]) ** 2
    i3 = int(valor1[2]) ** 2
    i4 = int(valor1[3]) ** 2
    i5 = int(valor1[4]) ** 2
    i6 = int(valor1[5]) ** 2
    i7 = int(valor1[6]) ** 2
    i8 = int(valor1[7]) ** 2
    i9 = int(valor1[8]) ** 2
    i10 = int(valor1[9]) ** 2

    valor2 = []
    valor2.extend([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10])

    print(valor1)
    print(valor2)
