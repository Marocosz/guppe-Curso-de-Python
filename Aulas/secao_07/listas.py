"""
Listas (list)

Listas em Python funcionam como vetores/matrizes, com a diferença de serem DINÂMICOS e também de
podermos colocar QUALQUER tipo de dado nelas.

    -É dinâmico pois não possui um tamanho fixo, ou seja, podemos criar a lista e adicionar elementos
    -Qualquer tipo de dado pois não tem um tipo fixo para ser adicionado

As listas em Python são representadas entre []
"""

"""
lista1 = [0, 99, 4, 26, 21, 62, 76, 2, 99, 4]

lista2 = ['g', 'q', ' ', 'as', 'h', 'K']

lista3 = []

lista4 = list(range(11))

lista5 = list('Marcos Rodrigues')

lista6 = ['Programação', 'em', 'Python', 'Essencial']

lista7 = [1, 2.34, 'amor', True, ['1','2', False], 1231255431245]  # Podemos misturar qualquer tipo de dado

cores = ['verde', 'amarelo', 'azul', 'branco']

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

    # Podemos facilmente checar se certo valor está contido na lista --------------------------------------------------

num = input('Digite o número que deseje achar: \n')

if num in lista1:
    print('Número encontrado')
else:
    print('Número não encontrado')


list_pass = [input('Digite a senha: \n')]

senha = 'abc123'

if senha in list_pass:
    print('Acesso permitido')
else:
    print('Acesso negado')


    # Podemos facilmente ordenar uma lista com o comando .sort() ------------------------------------------------------

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

     # Podemos facilmente contar o número de ocorrências de um valor numa lista com o comando .count(valor)-------------

print(lista1.count(99))
print(lista5.count('s'))

    # Podemos adiconar elementos em listas usando o comando .append()---------------------------------------------------

print(lista1)
lista1.append(42)
print(lista1)

# Porém, um valor apenas, mas podemos adicionar uma lista dentro de outra

lista1.append([1, 2, 3, 4])  # Utilazando o .append() dessa maneira, criamos uma sublista
print(lista1)

if [1, 2, 3, 4,] in lista1:
    print('Lista encontrada')
else:
    print('Lista não encontrada')

lista1.extend([12, 13, 14])  # Utilzando .extend() adicionamos valores e não uma sublista
print(lista1)                # aceita apenas valoers iteráveis

# Podemos inserir um novo elemento na lista informando a posição do índice utilizando .insert(posição, valor)
# E não há subistuição, o antigo valor '2' vai para direita

lista1.insert(2, 'Novo Valor')
print(lista1)

    # Podemos inverter a ordem da lista utilizando .reverse() ou [::-1] -----------------------------------------------

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

    # Podemos copiar uma lista utilizando o comando .copy() -----------------------------------------------------------

lista6 = lista4.copy()
print(lista4)
print(lista6)

    # Podemos contabilizar os elementos dentro de uma lista utilizando o comando .len() ------------------------------

print(len(lista5))

    # Podemos remover o último elemento de uma lista utilizando o comando .pop() -------------------------------------
    # OBS: O pop não apenas remove o último elemento, como também o retorna

print(lista5)
lista5.pop()
print(lista5)

    # Ou podemos também remover um elemento pelo índice utilzando .pop(número do índice)
    # E o índice da direita do elemento removido irá para esquerda

lista5.pop(2)
print(lista5)

   # Podemos remover todos os elementos utilizando o comando .clear() -----------------------------------------------


    # Podemos repetir elementos em uma lista utilizando a multiplicação -----------------------------------------------

nova = [1, 2, 3]
nova = nova * 3
print(nova)


    # Podemos transformar strings em listas ---------------------------------------------------------------------------

# Exemplo 01

curso = 'Programação em Python Pychamp'
print(curso)
curso = curso.split()
print(curso)

# Utilizando split, o padrão separa-se a lista por 'espaços'
# Mas podemos definir o separador por exemplo:

curso1 = 'Programação,em,python,pychamp'
print(curso1)
curso1 = curso1.split(',')    # Dessa forma, separará na virgula de acordo como definido
print(curso1)

    # Podemos converter lista em string utilizando o comando .join(lista) ----------------------------------------------

curso = ' ' .join(lista6)    # ' ' tendo o espaço em aspas para separar os itens da lista por espaço
print(curso)                 # Podemos escolher qualquer caractere para usar de separação

    # Iterando sobre listas -------------------------------------------------------------------------------------------

# Exemplo 01

soma = ''

for elemento in lista5:
    print(f'{elemento} ', end='')
    soma = soma + elemento

print('\n')
print(soma)

# Exemplo 02

carrinho = []
produto = ''

while produto != 'Sair':
    print('Adicione um produto na lista ou digite "Sair" para sair: ')
    produto = input()
    if produto != 'Sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

    # Utilizando variáveis em listas

num1 = 1
num2 = 2
num3 = 3
num4 = 4

numeros = [num1, num2, num3, num4]

    # Fazemos o acesso em elementos de forma indexada ------------------------------------------------------------------

#          0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])    # verde
print(cores[1])    # amarelo
print(cores[2])    # azul

    # Fazendo acesso aos elementos de forma indexada inversa ----------------------------------------------------------

print(cores[-1])    # branco
print(cores[-2])    # azul
print(cores[-3])    # amarelo

# Pensamos a lista como uma roda, o índice 0 se conecta ao ultimo indice
# formando então um circulo, onde do 0 a esquerda é negativo

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

    # Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)
    
    # Listas aceitam repetição
    
    # Outros métodos não tão importantes porém úteis

    # Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10, 5]

# Em qual índice da lista está o valor '6'
print(numeros.index(6))

# Em qual índice da lista está o valor '9'
print(numeros.index(9))

# OBS: Caso não tenha esse elemento será apresentado erro ValueError

# Quando há dois valores repetidos, o .index traz o primeiro encontrado
print(numeros.index(5))

    # Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar -----------------------------------

print(numeros.index(5, 1))    # .index(valor que deseja achar, a partir de qual indice procurar)

    # Podemos fazer busca dentro de um range com começo e fim ----------------------------------------------------------

print(numeros.index(8, 2, 5))    # Procurar o valor 8 entre os índices 2 e 5 

    # Revisão Slicing

# lista[inicio:fim:passo]
# range(indicio:fim:passo)

    # Trabalhando com o parâmentro 'ínicio' ---------------------------------------------------------------------------

lista = [1, 2, 3, 4]

print(lista[1:])    # Iniciando no índice 1 ao final e então printando isso
print(lista[:3])    # inciando do ínicio e indo ate o índice 3
print(lista[:-1])    # inciando do ínicio e indo ate o índice -1

# Utilizando o Passo
print(lista[1::2])    # Começando no índice 1, indo até o final, com passo de 2 em 2
print(lista[::-1])    # Começando do 0, indo até o final, e com passo -1

# Invertendo valores em uma lista --------------------------------------------------------------------------------------

nomes = ['Marcos', 'Rodrigues']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Marcos', 'Rodrigues']
nomes.reverse()
print(nomes)

    # Soma, valor máximo, valor mínimo e tamanho - Se valores inteiros ou reais-----------------------------------------

lista = [0, 1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Valor máximo
print(min(lista))  # Valor mínimo
print(len(lista))  # Tamanho da lista

    # Transformar lista em tupla---------------------------------------------------------------------------------------

lista = [0, 1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

    # Desempacotamento de listas --------------------------------------------------------------------------------------

lista = [1, 2, 3, 4]

num1, num2, num3, num4 = lista

print(num1)
print(num2)
print(num3)
print(num4)

# OBS: Se tiver mais elementos para desempacotar do que váriaveis pra receber os valoers dará ValueError e vice versa

    # Copiando uma lista para outra (Shallow Copy e Deep Copy) ---------------------------------------------------------

# Forma 01 - Deep Copy

lista = [1, 2, 3, 4]
print(lista)

nova = lista.copy()
print(nova)
nova.append(5)

print(lista)
print(nova)

# Utilizando .copy() a lista copiada é independente uma da outra, sendo assim chamada de Deep Copy

# Forma 02 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista
nova.append(4)

print(lista)
print(nova)

# Veja que, utilizando cópia via atribuição, as duas listas são modificadas quando há
# alteração em qualquer uma delas, sendo assim chamada de Shallow Copy
"""


