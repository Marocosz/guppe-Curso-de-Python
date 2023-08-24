"""
Mapas -> Conhecido como dicionário no Python

receita = {'jan': 100, 'fev': 250, 'mar': 400}

    # Iterando com dicionário -----------------------------------------------------------------------

for chave in receita:
    print(chave)  # Assim acessamos as chaves do dicionário

for chave in receita:
    print(receita[chave])  # Assim acessamos os valores do dicionário

for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}')  # Dessa forma conseguimos ver as chaves e os valores de cada chave


    # Acessando os elementos de um dicionário --------------------------------------------------------------------

print(receita.values())  # Assim conseguimos acessar os valores do dicionário

for valor in receita.values():
    print(valor)

print(receita.keys())  # Assim conseguimos acessar as chaves do dicionário

for chave in receita.keys():     # Modo Pythonico
    print(receita[chave])

    # Desempacotamento de dicionários --------------------------------------------------------------------

print(receita.items()) # Assim conseguimos acessar as chaves e os valores entre uma lista de tuplas

for chave, valor in receita.items():
    print(f'Chave = {chave} e valor = {valor}')
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# Sendo que * apenas se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
