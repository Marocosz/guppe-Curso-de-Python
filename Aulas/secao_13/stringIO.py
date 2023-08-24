"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissao:

   - Permissão de Leitura
   - Permissão de Escrita

StringIO -> Utilizado para ler e criar arquivos em memória
"""


# Para utilziar ========================================================================================================

# Primeiro Importamos

from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida, ou mesmo vazio, para inserirmos texto depois

arquivo = StringIO('String em memória')
# Equivalente a: arquivo = open('arquivo.txt', 'w')

# Agora podemos aplicar as funções de arquivos txt

let = arquivo.read()
print(let)
