"""
9. Faça um programa que receba dois arquivos do usuario, e crie um terceiro arquivo com
o conteudo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteudo do
segundo).
"""

arq = input('Digite o caminho do primeiro arquivo: ')
arq2 = input('Digite o caminho do segundo arquivo: ')
arq3 = input('Digite o nome do arquivo que deseja: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    lido = arquivo.read()

with open(arq2, 'r', encoding='utf-8') as arquivo2:
    lido2 = arquivo2.read()

with open(arq3, 'a+', encoding='utf-8') as arquivo3:
    arquivo3.write(f'{lido}\n')
    arquivo3.write(lido2)
    arquivo3.seek(0)
    print(arquivo3.read())