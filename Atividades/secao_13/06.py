"""
6. Faça um programa que receba doo usuário um arquivo texto e mostre na tela quantas
vezes cada letra do afabeto aparece dentro do arquivo.
"""
arquivo = input('Digite o caminho do arquivo que deseje analisar: ')

with open(arquivo, 'r', encoding='utf-8') as arq:
    char = arq.read()
    dic = dict()
    for x in char:
        count = 0
        for y in char:
            if y == x:
                count += 1
        dic[x] = count

print(dic)

