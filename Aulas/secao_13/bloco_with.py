"""
O bloco with

Passo para o trabalho em arquivos:

1 - Abrimos o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados
após o block with
"""

# Exemplo ==============================================================================================================

with open('texto.txt', encoding='utf-8') as arquivo:  # Com o arquivo 'texto.txt', chamado arqvuio, faça:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)

# Dessa forma, o arquivo é fechado logo após manipulado dentro do bloco with
