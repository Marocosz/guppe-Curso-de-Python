"""
**Kwargs

A função pode ter: (NESSA ORDEM)

- Parâmetros obrigatórios
- *args
- Parâmetros não obrigatórios
- **kwargs

OBS: **Kwargs funcionam como dicionários

Este é um parâmetro, mas diferente do *args, que coloca os valores extras em uma tupla, o **kwars exige que utilizemos
parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

OBS: Os **kwargs não são obrigatórios

    # Exemplo ---------------------------------------------------------------------------------------------------------


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos ='verde', heloisa='preto', arthur='branco')

    # Exemplo mais complexo -------------------------------------------------------------------------------------------

def cumprimento_especial(**kwargs):
    if 'Marcos' in kwargs and kwargs['Marcos'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'Marcos' in kwargs:
        return f'{kwargs["Marcos"]} Marcos!'
    else:
        return 'Não tenho certeza de quem é você'

print(cumprimento_especial())
print(cumprimento_especial(Marcos='Marcos'))
print(cumprimento_especial(Marcos= 'Python'))
print(cumprimento_especial(Marcos= 'Rodrigues'))

    # Função com todos os tipos de parâmetros -------------------------------------------------------------------------


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(18, 'Marcos', 4, 5, 6, solteiro=True, eu='sim', não='ok')

    # Desempacotando **Kwargs -----------------------------------------------------------------------------------------

def mostra_nome(**kwargs):
    return f'{kwargs["nome"]}, {kwargs["sobrenome"]}'


nomes = {'nome': 'Marcos', 'sobrenome':'Rodrigues'}

print(mostra_nome(nome='Marcos', sobrenome='Rodrigues'))

print(mostra_nome(**nomes))  # Desempacotou a variável


# Desempacotando **Kwargs 2 -----------------------------------------------------------------------------------------

def soma(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]  # Pode ser lista, conjunto ou tupla

soma(*lista)

dic = dict(a=1, b=2, c=3)

soma(**dic)

# OBS: Os nomes das chaves em um dicionário devem ser o mesmo dos parâmetros da função
"""



def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(18, 'Marcos', 4, 5, 6, solteiro=True, eu='sim', não='ok')