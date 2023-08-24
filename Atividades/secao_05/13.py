p1 = float(input('Digite sua pontuação na primeira prova:'))
pe1 = float(input('Digite o peso da primeira prova:'))

p2 = float(input('Digite sua pontuação na segunda prova:'))
pe2 = float(input('Digite o peso da segunda prova:'))

p3 = float(input('Digite sua pontuação na terceira prova:'))
pe3 = float(input('Digite o peso da terceira prova:'))

mediap = ((p1 * pe1) + (p2 * pe2) + (p3 * pe3)) / (pe1 + pe2 + pe3)

print(f'A média pontuada é {round(mediap, 2)}')
