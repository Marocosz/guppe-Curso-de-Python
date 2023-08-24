soma = 0

for n in range(3):
    numero = float(input('Digite sua nota aqui:'))
    if 10 < numero < 20:
        soma = soma + numero
    else:
        print('Sua nota deve ser entre 10 e 20')

print(f'A média de sua nota é {soma / 3}')
