"""
Tuplas (tuple)

# Porque usar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro ( Isso porque trabalhar com elementos imutáveis traz segurança)

Tuplas são bastantes parecidas com listas
Existem basicamente 2 diferenças

1- As tuplas são representadas por ()
2- As tuplas são imutáveis: isso significa que, ao se criar uma tupla, ela não muda. Toda
Operação em uma tupla, gera uma nova tupla.

    # Cuidado 01: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

    # Cuidado 02: Tuplas com 1 elemento:

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

# Conclusão, podemos definir que uma tupla é definida pela vírgula e não pelo parentese

tupla5 = 4,
print(tupla5)
print(type(tupla5))

    # Podemos gerar uma tupla utilizando range -------------------------------------------------------------

tupla = tuple(range(11))
print(tupla)

    # Desempacotamento de tupla -------------------------------------------------------------

tupla = ('Marcos', 'Rodrigues')
nome, sobrenome = tupla

print(nome)
print(sobrenome)

# OBS: Se colocar um número de variavel diferente do número de elementos da tupla, dará erro

# Métodos para adição e remoção de elementos nas tuplas não existem, pelo fato de serem imutáveis

# Soma*, Valor Máximo*, Valor Mínimo*, e Tamanho

# * Se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

    # Contatenação de tuplas -------------------------------------------------------------

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2     # Tuplas são imutaveis mas pode sobreescrever seu valor
print(tupla1)

    # Encontrar determinado valor em uma tupla -------------------------------------------------------------

tupla = (1, 2, 3)

print(3 in tupla)

    # Iterando sobre uma tupla -------------------------------------------------------------

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

    # Contando elementos dentro de uma tupla -------------------------------------------------------------

tupla = ('a','b', 'a', 'c')

print(tupla.count('a'))

nome = tuple('Marcos Rodrigues')

print(nome)
print(nome.count('s'))

    # Precisamos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 01

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Outubro', 'Novembro', 'Dezembro')
print(len(meses)+1)

# O acesso de elementos de uma tupla é semelhante a de uma lista

print(meses[5+1])

# Iterando com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1


meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Outubro', 'Novembro', 'Dezembro')
print(len(meses)+1)

   # Verificando em qual índice um elemento está na tupla -------------------------------------------------------------

print(meses.index('Junho'))

# OBS: Casos o elemento não exista, dará ValueError

    # Slicing

# tupla[inicio:fim:passo]

    # Copiando uma tupla para outra -------------------------------------------------------------

tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(outra)
print(nova)
print(tupla)

# Não há Shallow Copy na tupla

    # Criando tuplas de outras tuplas ---------------------------------------------------------------------------

produto1 = ('Playstation 04', 1, 5000.00)
produto2 = ('God of War 04', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
"""
