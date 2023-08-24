"""
Escopo de Variáveis

1- Variáveis Globais
    - Variavéis globais são reconhecidas, ou seja, seu escopo compreende todo o programa

2- Variáveis Locais
    - Já as variáveis locais são reconhecidas apenas no bloco onde foram declaradas , ou seja,
    seu escopo está limitado ao bloco onde foi declarada

Para declaração de variável no Python, fazemos:

nome_da_variavel = valor_da_variavel

ex: numero = 42

Python é uma linguagem de tipagem dinâmica, ou seja, o tipo de dado da variável é atribuído
referente ao seu valor

Ex em C:
int numero = 42;

Ex em Java
int numero = 42;

Ex em Python
numero = 42


nome = 'Marcos'  # Variável Global

if nome != 'Marcos':
    erro = 'Incorreto'    # 'erro' é uma variável local
    print(erro)
"""
