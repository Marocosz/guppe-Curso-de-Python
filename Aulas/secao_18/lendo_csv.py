"""
Lendo arquivos CSV

CSV - Comma Separeted Values (Valores Separados por Vírgula)

Site para pegar dados: https://dados.gov.br/dataset

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV
    - Reader -> Permite que iteremos sobre as linhas como listas
    - DictReader -> Permite que iteremos sobre as linhas como OrderedDicts


# Trabalhoso de se ler csv =============================================================================================

with open('C:\\Users\\marco\\PycharmProjects\\guppe\\Outros\\lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

"""

# Reader ===============================================================================================================

from csv import reader

with open('C:\\Users\\marco\\PycharmProjects\\guppe\\Outros\\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')


# Dict Readr ===========================================================================================================

from csv import DictReader

with open('C:\\Users\\marco\\PycharmProjects\\guppe\\Outros\\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")

    # Usamos os itens do cabeçalho como chave dos valores

# Por padrão, o reader separa os valores pela vírgula, mas podemos alterar adicionando um parâmetro
# Dessa forma: leitor_csv = DictReader(arquivo, delimiter=';')
