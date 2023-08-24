"""
3. Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas
letras são vogais.
"""
vogais = 'aeiouáéíóúâêîôûãõàèìòùÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙAEIOU'
listavogais = []

arq = input('Digite o caminho do arquivo que deseje contar as vogais: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    lido = arquivo.read()
    for x in lido:
        if x in vogais:
            listavogais.append(x)

    print(f'A quantidade de vogais do seu arquivo é: {len(listavogais)}, sendo elas: {set(listavogais)}')
