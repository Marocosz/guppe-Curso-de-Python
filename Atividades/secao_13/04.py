"""
4. Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas
letras são vogais e quantas são consoantes.
"""
vogais = 'aeiouáéíóúâêîôûãõàèìòùÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙAEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
listavogais = []
listaconsoantes = []

arq = input('Digite o caminho do arquivo que deseje contar as vogais e consoantes: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    lido = arquivo.read()
    for x in lido:
        if x in vogais:
            listavogais.append(x)
        elif x in consoantes:
            listaconsoantes.append(x)

    print(f'A quantidade de vogais do seu arquivo é: {len(listavogais)}, sendo elas: {listavogais}')
    print(f'E a quantidade de consoantes do seu arquivo é: {len(listaconsoantes)}, sendo elas: {listaconsoantes}')