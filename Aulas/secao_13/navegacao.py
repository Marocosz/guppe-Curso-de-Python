"""
Sistema de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do modúlo 'os'

os -> Sistema Operacional


# Exemplo ==============================================================================================================

import os

# getcwd() -> Pega o current work directory (Diretório de trabalho corrente)
# retorna o path (caminho) absoluto

print(os.getcwd())  # C:\\Users\\marco\\PycharmProjects\\guppe\\Aulas\\secao_13

# chdir() -> Mudamos de diretório

os.chdir('..')  # '..' para voltarmos de diretório

print(os.getcwd())  # C:\\Users\\marco\\PycharmProjects\\guppe\\Aulas


# Checando se o diretório é absoluto ou relativo =======================================================================

import os

print(os.path.isabs('C:\\Users\\marco\\PycharmProjects\\guppe\\Aulas'))  # True = Absoluto
print(os.path.isabs('C:\\Users'))  # True = Absoluto


# Identificar o OS =====================================================================================================

import os, platform

print(os.name)  # windos = nt, linux e ios = posix

# Mais detalhes o OS:

print(platform.uname())  # Usa platform para windows e os para linux e ios


# Mudar de diretórios ==================================================================================================

import os

print(os.getcwd())  # C:\\Users\\marco\\PycharmProjects\\guppe\\Aulas\\secao_13

os.chdir('C:\\Users\\marco\\PycharmProjects')

print(os.getcwd())  # C:\\Users\\marco\\PycharmProjects

var = os.path.join(os.getcwd(), 'guppe')

print(var)  # C:\\Users\\marco\\PycharmProjects\\guppe

os.chdir(var)

print(os.getcwd())  # C:\\Users\\marco\\PycharmProjects\\guppe

# OBS: Vemos que o 'os.path.join' recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo
# o diretório que será juntado ao atual


# Listar os arquivos do diretório ======================================================================================

import os

# Utilizando o 'os.listdir()' ele retorna em lista os arquivos/diretórios dentro de um diretório

print(os.listdir())

os.chdir('..')

print(os.listdir())

print(os.listdir('c:\\users\\marco'))

# Scan =================================================================================================================

import os

scanner = (os.scandir())
arquivos = list(scanner)

print(arquivos)  # Lista de 'DirEntry' do diretório
print(arquivos[0])  # Primeiro elemento da lista do diret´orio
print(arquivos[0].name)  # Nome do primeiro elemento da lista do diretório
print(arquivos[0].path)  # Endereço de caminho
print(arquivos[0].stat)

# É importante fehcar o scandir se utiliza-lo

scanner.close()

# Entre outras funções
"""




