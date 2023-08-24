print('Escreva suas duas notas para conferir')
nota1 = float(input())
nota2 = float(input())

if nota1 > 0 and nota2 > 0:
    if nota1 < 11 and nota2 < 11:
        media = (nota1 + nota2) / 2
        print(f'A média de sua nota é {media}')

    else:
        print('Erro')
        
else:
    print('Erro')
