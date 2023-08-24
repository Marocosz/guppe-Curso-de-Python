"""
Faça um programa no qual o usuario intorma o nome do arquivo e uma palavra, e retorne
o numero de vezes que aquela palavra aparece no arquivo.
"""

arq = input('Informe o arquivo que deseja analisar: ')
palavra = input('Informe a palavra que deseja achar: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    count = 0
    listatotal = []
    for x in linhas:
        separado = x.split(' ')
        listatotal.append(separado)
    for x in listatotal:
        for y in x:
            if palavra in y:
                count += 1

print(f'A palavra: {palavra}, apareceu {count} vezes em seu arquivo')