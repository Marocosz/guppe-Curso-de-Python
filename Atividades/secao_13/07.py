"""
7 Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto
contendo o texto do arquivo de entrada, mas com as vogais substituídas por *.
"""


arq = input('Digite o caminho do arquivo que desejar escanear: ')

vogais = 'aeiouáéíóúâêîôûãõàèìòùÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙAEIOU'

with open(arq, 'r', encoding='utf-8') as arq:
    char = arq.read()
    for x in char:
        if x in vogais:
            char = char.replace(x, '*')
    print(char)
