"""
2. Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas
innas esse arquivo possui.
"""

arq = input('Digite o caminho do arquivo que deseje contar as linhas: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    listlinha = arquivo.readlines()
    print(f'A quantidade de linhas do seu arquivo é: {len(listlinha)}')
