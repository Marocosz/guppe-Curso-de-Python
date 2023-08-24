"""
Sistema de Arquivos - Manipulação


# Descobrindo se um arquivo/diretório existe ===========================================================================

import os

print(os.path.exists('arquivo.txt'))  # False - Não existe  (relativo)
print(os.path.exists("C:\\Users\\marco\\Desktop\\backup"))  # True - Existe   (absoluto)


# Criando arquivos =====================================================================================================

import os

# Forma 01
open('C:\\Users\\marco\\Desktop\\arquivo_teste.txt', 'w').close()

# Forma 02
open('C:\\Users\\marco\\Desktop\\arquivo_teste2.txt', 'a').close()

# Forma 03
with open('C:\\Users\\marco\\Desktop\\arquivo_teste3.txt', 'w') as arquivo:
    pass


# Criando Diretórios ===================================================================================================

import os

os.mkdir('C:\\Users\\marco\\Desktop\\diretorio')

# OBS: A função 'mkdir()' cria um diretório se não existir, caso exista, dará o erro 'FileExistsError'

# OBS: Só podemos criar um diretório por vez

# Para criar mais de um de uma vez:

os.makedirs('C:\\Users\\marco\\Desktop\\teste1\\teste2')

os.makedirs('C:\\Users\\marco\\Desktop\\teste1\\teste2', exist_ok=True)  # Com esse segundo parâmetro, caso o path
                                                                         # já exista, ele ira ignorar

# Renomear arquivos e diretórios =======================================================================================

import os

os.rename('C:\\Users\\marco\\Desktop\\diretorio', 'C:\\Users\\marco\\Desktop\\pasta')

# Sendo o primeiro parâmetro o arquivo que deseja renomear o segundo como deseja renomear


# Deletar arquivos =====================================================================================================

# ATENÇÃO! Cuidado com os comandos de deleção
# Ao deletarmos um arquivo/diretório ele não ira para a lixeira, serão excluídos permanentemente

import os

open('C:\\Users\\marco\\Desktop\\arquivo.txt', 'w').close()

os.remove('C:\\Users\\marco\\Desktop\\arquivo.txt')

# OBS: Se não existir o arquivo que tentar deletar, dará o erro FileNotFoundError
# OBS: Se estiver no Windows e o arquivo que deseja deletar estiver em uso, dará erro
# OBS: Essa função serve apenas para deleção de arquivos e não diretórios


# Deletar diretórios ===================================================================================================

import os

# os.mkdir('C:\\Users\\marco\\Desktop\\pasta')

os.rmdir('C:\\Users\\marco\\Desktop\\pasta')

# OBS: Se houver arquivos do diretório, ocorrerá o erro OSError
# OBS: Se o diretório não existir, ocorrerá o erro FileNotFoundError


# Remover uma árvore de diretórios =====================================================================================

import os

for arquivo in os.scandir('C:\\Users\\marco\\Desktop\\pasta1'):
    print(arquivo.path)

    if arquivo.is_file():
        os.remove(arquivo)

    if not arquivo.is_file():
        os.rmdir(arquivo)


# Enviando diretórios/arquivos para a lixeira ==========================================================================

# Teriamos que instalar um pacote que se chama send2trash
# pip install send2trash

from send2trash import send2trash as trash

trash("C:\\Users\\marco\\Desktop\\pasta1")

# OBS: Se o arquivo não existir, terá OSError


# Criando diretórios temporários =======================================================================================

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'pasta1.txt'), 'w') as arquivo:
        arquivo.write('Marcos Rodrigues\n')
    input()

# Com esse código, utilizando o comando 'tempfile.TemporaryDirectory()' criamos um diretório temporario
# Onde dentro dele com o código 'open(os.path.join(tmp, 'pasta1.txt'), 'w')', onde a função 'open()' serve para
# criação de arquivos, e utilizando o 'os.path.join' que serve para a junção de caminho (path)
# dentro do outro bloco with ele escreverá 'Marcos Rodrigues\n' com a função '.write()'
# E por estar em um bloco with, esse diretório temporário acabará ao input ser realizado


# Criando arquivos temporários =========================================================================================

import os
import tempfile

with tempfile.NamedTemporaryFile() as tmp:
    print(tmp.name)
    tmp.write(b'Marcos Rodriges\n')
    tmp.seek(0)
    print(tmp.read())
    input()

# OBS: Em arquivos temporários só conseguimos escrever bits, po isso, utilizamos 'b' antes do que queremos
"""
