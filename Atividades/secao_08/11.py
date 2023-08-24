def nota(nota1, nota2, nota3, letra):
    if letra == 'A':
        ma = (nota1 + nota2 + nota3) / 3
        return f'A média do aluno é {ma}'
    elif letra =='P':
        mp = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2) / (5 + 3 +2))
        return f'A média do aluno é {mp}'


print(nota(10, 12, 8, 'A'))
print(nota(20, 19, 2, 'P'))
