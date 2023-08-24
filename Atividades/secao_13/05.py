"""
5. Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.
"""

quant = []

arq = input('Digite o caminho do arquivo que deseje contar: ')
letra = input('Digite a letra que deseja procurar em seu arquvio: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    lido = arquivo.read()
    for x in lido:
        if x in letra:
            quant.append(x)

    print(f'A letra "{letra}", aparece {len(quant)} vezes no seu arquivo')
