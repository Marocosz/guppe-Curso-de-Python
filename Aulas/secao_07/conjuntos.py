"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos da Matemática

- Aqui no Python os conjuntos são chamados de Sets.
- Dito isso, da mesma forma que na Matemática:

    -Sets(Conjuntos) não possuem valores duplicados
    -Sets(Conjuntos) não possuem valores ordenados
    -Elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para utilizar quando precisamos armazenar elementosmas não nos
importamos com a ordenação deles. Quando não precisamos se importar com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados com {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python

    -Um Dicionário tem chave/valor
    -Um Conjunto tem apenas valor

    # Definindo um conjunto ------------------------------------------------------------------------------------------

# Forma 01

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valoers repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será
# ignorado e não fará parte do conjunto, não gerando erro.

# Forma 02 (Mais comum)

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


    # Verificando se determinado elemento tem no conjunto -------------------------------------------------------------

if 3 in s:
    print('Tem o número 3')
else:
    print('Nao tem o número 3')

# Importante lembrar que, além de não ter valores duplicados, também não há ordem

lista = [99, 2, 34, 23, 12, 1, 44, 2, 34]
print(f'lista {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 12, 1, 44, 2, 34)
print(f'tupla {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'dicionário {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados e ordena de sua forma
conjunto = {99, 2, 34, 23, 12, 1, 44, 2, 34}
print(f'conjunto {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python, podemos colocar todos tipos de dados misutrados em Sets

s = {1, 'b', True, 32.22, 44}
print(s)

    # Iterando sobre conjuntos --------------------------------------------------------------------------------------

for valor in s:
    print(valor)

    # Usos interessantes com Sets -----------------------------------------------------------------------------------

# Imagine que fizemos um formulário de cadastro de vistantes de um museu, e os visitantes informam manualmente
# a cidade de onde vieram, nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar
# novos elementos e ter repetição

cidades = ['São Paulo', 'Belo Horizonte', 'Campo Grande', 'Cuiaba', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas temos
# Podemos usar o Sets para isso

print(len(set(cidades)))

    # Adicionando elementos em conjunto -----------------------------------------------------------------------------

s = {1, 2, 3}
s.add(4)
print(s)
# Duplicidade não gera erro, apenas é ignorado

    # Removendo elementos em conjunto ------------------------------------------------------------------------------

s = {1, 2, 3}

# Forma 01

s.remove(3)  # Não é indice e sim valor!!!!!
print(s)

# OBS: Caso não há o valor, gerará um KeyError, e também não há retorno de valor

# Forma 02

s.discard(2)
print(s)

# OBS: Dessa forma, mesmo não havendo o valor, não terá erro nenhum

    # Copiando um conjunto para outro --------------------------------------------------------------------------------

s = {1, 2, 3}
print(s)

# Forma 01 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)
print(s)
print(novo)

# Forma 0 - Shallow Copy

s = {1, 2, 3}
print(s)

novo = s
print(novo)

novo.add(4)
print(novo)
print(s)

    # Removendo todos elementos do conjunto ---------------------------------------------------------------------

s = {1, 2, 3}
print(s)

s.clear()
print(s)

    # Métodos Matemáticos de Conjuntos -----------------------------------------------------------------------------

# Imagine que temos dois conjuntos, um contendo os estudantes de python e o outro os estudantes de java

estudantes_python = {'Marcos', 'Patricía', 'Elen', 'Julia', 'Guilherme', 'Ana'}
estudantes_java = {'Fernando', 'Gustavo', 'Ana', 'Roberto', 'Julia'}

# Veja que alguns alunos que estudam Python tambem estudam Java

# Precisamos gerar um conjunto com nomes de estudantes totais

# Forma 01 - Utilizando Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 02 - Usando caractere pipi '|'

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Precisamos agora gerar um conjunto de estudantes que estão em ambos cursos

# Forma 01 - Utilizando Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 02 - Utiliando o '&'

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Agora precisamos gerar um conjunto de estudantes que não estão em outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

    # Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
    # * se forem inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
