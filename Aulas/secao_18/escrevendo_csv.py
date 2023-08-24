"""
Escrevendo em arquivos CSV

writer() -> gera um objeto para escrever
writerow() -> Escreve uma linha


# Writer ===============================================================================================================

from csv import writer

with open('filmes.csv','w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])
"""


# DictWriter ===========================================================================================================

# OBS: As chaves do dicionário devem ser as mesmas usadas no cabeçalho

from csv import DictWriter

with open('filmes1.csv', 'w', encoding='utf-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()  # Escrever o cabeçalho no arquivo
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
