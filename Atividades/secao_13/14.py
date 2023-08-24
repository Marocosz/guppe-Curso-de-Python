"""
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data
de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro
arquivo.
"""

from datetime import date

data_a = date.today()
data_atual = '{} {} {}'.format(data_a.day, data_a.month, data_a.year)
data_atual_list = data_atual.split()

arq = input('Digite o caminho do arquivo que deseja analisar: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        separado = linha.split()
        resultado = int(data_atual_list[2]) - int(separado[3])
        if int(data_atual_list[1]) < int(separado[2]):
            resultado -= 1
        if int(data_atual_list[1]) == int(separado[2]):
            if int(data_atual_list[0]) < int(separado[1]):
                resultado += 1

        print(f'{separado[0]} tem {resultado} anos')
