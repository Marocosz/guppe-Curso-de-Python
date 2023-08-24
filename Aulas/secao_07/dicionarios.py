"""
Dicionários

OBS: NÂO HÁ REPETIÇÃO DE CHAVES

OBS: Em algumas linguagens de programação, dicionários Python, são conhecidos como Mapas

Dicionários são coleções do tipo chave/calor

Dicionários são representados por {}

OBS: Sobre dicionários

    - Chave e valor são separados por 'chave':'valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

# Forma 01: (Mais comum)
paises = {'br':' Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 02: (Menos comum)

paises = dict(br= 'Brasil', eua= 'Estados Unidos', py= 'Paraguai')

print(paises)
print(type(paises))

    # Acessando elementos ----------------------------------------------------------------------------------

# Forma 01 - Via chave, da mesma forma que lista/tupla
print(paises['br'])

# OBS: Se tentarmos acessar uma chave inexistente terá KeyError

# Forma 02 - Acessando via Get (Recomenadado)
print(paises.get('br'))
print(paises.get('ru'))

# OBS: Dessa forma não há erro, porém chega o tipo de dado 'None'

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('br', 'Não encontrado')

print(f'Encontrei o pais {pais}')

# Podemos definir um valor padrão para o caso de não encontrar o valor da chave informada

paises = {'br':' Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    # Verifica se determinada chave está dentro do dicionário --------------------------------------------------------

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Essa busca é feita pela chave do Dict, não pelo valor

    # Podemos usar qualquer tipo de dado em um dicinário QUALQUER TIPO

    # Tuplas são bem interessantes para utilizar em chaves de dicionários, pois elas são imutáveis

localidades = {
    (35.4732, 23.3523): 'Escritório em Tokio',
    (23.2312, 89.2002): 'Escritório em Nova York',
    (69.2333, 70.7892): 'Escritório em São Pualo',
}

print(localidades)
print(type(localidades))

    # Adicionar elementos em um dicionário --------------------------------------------------------------------

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 01 (Mais comum)

receita['abr'] = 350
print(receita)

# Forma 02

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.updade({'mai': 500})
print(receita)

    # Atualizando dados em um dicionário --------------------------------------------------------------------

# Forma 01

receita['mai'] = 550
print(receita)

# Forma 02

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: forma de atualizar elementos ou adicionar novos elementos é a mesma
# CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetidas

    # Remover dados de um dicionário --------------------------------------------------------------------

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# FOrma 01 (Mais comum)

ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento,um KeyError será retornado
# OBS 2: Ao removermos um objeto com o .pop, o valor desse objeto é retornado

# Forma 02

del receita['fev']
print(receita)

# Se a chave não existir gerará um KeyError
# OBS: Neste caso não há retorno de valor diferente da forma 01

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos  produtos --------

Carrinho de Compras:
    Produto 01:
        - nome:
        - quantidade:
        - preço:
    Produto 02:
        - nome:
        - quantidade:
        - preço:

# 1 - Poderiamos fazer com lista

carrinho = []

produto1 = ['Playstation 04', 1, 5000.00]
produto2 = ['God of War 04', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação do produto

# 2 - Poderiamos fazer com tuplas

produto1 = ('Playstation 04', 1, 5000.00)
produto2 = ('God of War 04', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação do produto

# 3 - Poderiamos fazer com dicionário

carrinho = []

produto1 = {'nome': 'Playstation 04', 'quantidade': 1, 'preço': 5000.00}
produto2 = {'nome': 'God of War 04', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print(type(carrinho))

# Desta forma facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza e fácil visualização de cada informação

    # Comandos para o Dicionário --------------------------------------------------------------------------------

    # Limpar o Dicionário --------------------------------------------------------------------------------

d = dict(a=1, b=2, c=3)
d.clear()
print(d)

    # Copiando um dicionário para outro -----------------------------------------------------------------------------

# Forma 01:  Deep Copy

d = dict(a=1, b=2, c=3)

novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)
print(d)

# Forma 02:  Shallow Copy

d = dict(a=1, b=2, c=3)

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

    # Forma não usual de criar dicionário

outro = {}.fromkeys('A', 'a')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nomes', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metódo 'fromkeys' recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave, e irá atribuir a estas chaves o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)

"""
