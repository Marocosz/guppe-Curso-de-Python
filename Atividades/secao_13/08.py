"""
8. Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo
conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os no-
mes dos arquivos serão fornecidos, via teclado, pelo usuário. A função que converte
maiúscula para minúscula é o toupper). Ela é aplicada em cada caractere da string
"""

arq = input('Digite o caminho do arquivo que deseja copiar: ')
arq2 = input('Digite o caminho com o nome do novo arquivo: ')

with open(arq, 'r', encoding='utf-8') as arquivo:
    lido = arquivo.read()

with open(arq2, 'a+',encoding='utf-8') as arquivo2:
    arquivo2.write(lido.upper())
    arquivo2.seek(0)
    print(arquivo2.read())
