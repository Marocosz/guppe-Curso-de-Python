tl = float(input('Pontuação do Trabalho de Laboratório:'))
As = float(input('Pontuação da Avaliação Semestral:'))
ef = float(input('Pontuação do Exame Final:'))

mediap = ((tl * 2) + (As * 3) + (ef * 5)) / (2 + 3 + 5)

if tl < 0 or As < 0 or ef < 0:
    print('Sua pontuação deve ser entre 0 e 10.')

elif tl > 10 or As > 10 or ef > 10:
    print('Sua pontuação deve ser entre 0 e 10.')

else:
    if mediap < 3:
        print(f'Sua média foi {mediap}. Portanto, reprovado.')
    elif mediap < 5:
        print(f'Sua média foi {mediap}. Portanto, recuperação.')
    else:
        print(f'Sua média foi {mediap}. Portanto, aprovado.')
