"""
Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O
arquivo de entrada contem em cada linhao nome de uma cidade (ocupando 40 caracte
res) e o seu número de habitantes. O programa deverá ler o arquivo de entrada e gerar
um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu
número de habitantes.
"""

arq = input('Digite o caminho do arquivo que deseja analisar: ')
arq2 = input('Digite o nome que o novo arquivo terá: ')

filtro = '\n'
max = 0

with open(arq, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    dic = dict()
    for x in linhas:
        separado = x.split(': ')
        for y in separado[1]:
            if y in filtro:
                separado[1] = separado[1].replace(y, '')
                separado[1] = int(separado[1])
                dic[separado[0]] = separado[1]

maior = ''
for key, value in dic.items():
    if value > max:
        max = value
        maior = f'A maior cidade é {key} com {value} habitantes'

with open(arq2, 'a+', encoding='utf-8') as arquivo2:
    arquivo2.write(maior)
    arquivo2.seek(0)
    print(arquivo2.read())



