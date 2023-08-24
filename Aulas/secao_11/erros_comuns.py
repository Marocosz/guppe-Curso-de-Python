"""
Erros mais comuns em Python

# É importante prestar atenção na saída de erros, e também aprender a lê-las

Os erros:

1- SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, escreveu algo que o Python não
reconhece como parte da Linguagem

2- NameError -> Ocorre quando uma variável ou função não foi definida

3- TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplo

soma = 'a' * 'b'  # Não há como multiplicar strings


4- IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um índice invalido

# Exemplo

lista = [1, 2, 3]

print(lista[4])  # Lista há apenas 3 elementos, ou seja, não há como acessar o quarto índice

5- ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo
correto, mas valor inapropriado

# Exemplo

print(int('Marcos'))  # A função 'int' espera receber um valor que possa ser convertido em int, como um número

6- KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

7- AttributeError -> Occore quando uma variável não tem um atributo ou função

8- IndentationError -> Ocorre quando não respeitamos a identação do python (4 espaços)

"""



