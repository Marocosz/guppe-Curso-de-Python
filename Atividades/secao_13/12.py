"""
12. Abra um arquivo texto, calcule e escreva o número de caracteres, o numero de linhas e
o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais
caracteres espaço, tabulação ou nova linha.
"""

import string

nome_arquivo = input('Digite o nome do arquivo. Formato nome.extensão: ')
dicionario = dict()

with open(nome_arquivo, 'r', encoding="UTF-8") as arquivo:
    caracter = str(arquivo.read())
    arquivo.seek(0)
    palavra = arquivo.read().split()
    arquivo.seek(0)
    print(f'A quantidade de caracteres: {len(caracter)}')
    print(f'A quantidade de linhas: {len(arquivo.readlines())}')
    print(f'A quantidade de palavras: {len(palavra)}')
    print(f'A quantidade de cada letra do alfabeto no texto (caracteres acentuados serão ignorados): ')
    [dicionario.update({letra: caracter.lower().count(letra)}) for letra in caracter.lower() if letra in string.ascii_letters]
    for key, value in sorted(dicionario.items()):
        print(f'{key} - {value}')