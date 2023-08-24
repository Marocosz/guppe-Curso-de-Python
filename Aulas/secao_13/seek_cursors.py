"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo, onde ela recebe o parâmetro que
indica onde estará o cursor

# OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada streaming. E ao finalizar os trabalhos com o arquivo, devemos fechar
essa coenxão utilizando a função close()


# Passos para se trabalhar com um arquivo ==============================================================================

# 1 - Abrir o arquivo
arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar com o arquivo
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está fechado ou não (True ou False)

# 3 - Fechar o arquivo
arquivo.close()


# Movimentando o cursor ================================================================================================

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

arquivo.seek(0)  # Dessa forma voltamos o cursor para o ínicio do arquivo, assim podendo printar o 'read()' novamente

print(arquivo.read())

arquivo.seek(19)  # Cursor está no caractere 19

print(arquivo.read())


# Função readline() ===================================================================================================

# readline() -> Função que lê o arquivo linha a linha

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.readline())  # linha 1
print(arquivo.readline())  # linha 2
print(arquivo.readline())  # linha 3
print(arquivo.readline())  # linha 4

ret = arquivo.readline()

print(ret)
print(type(ret))
print(ret.split(' '))


# Função readlines() ===================================================================================================

# readlines() -> Torna cada linha do arquivo em um elemento de uma lista

arquivo = open('texto.txt', encoding='utf-8')

linhas = arquivo.readlines()

print(linhas)
print(len(linhas))


"""






