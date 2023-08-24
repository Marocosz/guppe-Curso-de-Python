"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada
que nesse caso é o caminho do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
e é com ele que trabalhamos

https://docs.python.org/pt-br/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então terá erro

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Significa modo de leitura


# Exemplo ==============================================================================================================

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo)
print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura devemos utilizar a função read()

print(arquivo.read())  # Lê todo o conteúdo do arquivo

# E ele é lido apenas uma vez

# OBS: O Python, utiliza um recurso para trabalhar com arquivo chamado cursor. Esse cursor, funciona
# como o cursor quando estamos escrevendo.


# Abrindo por diretório externo ========================================================================================

arquivo2 = open('C:\\Users\\marco\\Desktop\\deste.txt',  encoding='utf-8')

# Utilizamos o r' antes para o Python entender que é o um caminho de arquivo, ou então podemos usar \\ em vez de \

print(arquivo2.read())


# Podemos limitar a leitura ============================================================================================

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read(50))  # Limitamos a leitura até o 50 caractere

"""





