# Criar um dic:

dic1 = {'a': [1, 2], 'b': 2, 'c': 3}
dic2 = dict(a=1, b=2, c=3)

print(len(dic1['a']))

# Acessar algum valor

print(dic1['a'])
print(dic1.get('a'))

# Achar alguma chave

print('a' in dic1)

# Adicionar ou atualizar um elemento

dic1['d'] = 4
dic2.update({'d': 4})

# Remover um elemento

dic1.pop('d')
del dic1['a']

# Copiar um dicionario

a = dic1.copy()  # Deep Copy

b = dic2  # Shallow Copy

# Lista de tuplas do dicionário

h = dic2.items()
print(b)

# Valores do dicionário em lista

c = dic2.values()
print(c)

# Limpar um dicionario

dic1.clear()