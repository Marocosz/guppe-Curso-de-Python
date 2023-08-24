"""
Módulo Collections - Default Dict

# Recap Dicionários

dicionario = {'nome': 'Marcos Rodrigues'}
print(dicionario)

print(dicionario['nome'])

print(dicionario['outro])  # KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nos criamos um valor default, podendo utilizar um lambda
para isso. Esse valor será utilizando sempre que não ouver um valor definido e caso tentarmos acessar uma
chave inexistente, essa chave será criada e o valor default será atribuído.


"""

    # Fazend o Import----------------------------------------------------------------------------------------

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['Nome'] = "Marcos Rodrigues"
print(dicionario)

print(dicionario['Outro'])  # Daria um keyError, mas com o default dict acontece outra coisa

print(dicionario)

