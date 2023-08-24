"""
Estruturas lógicas
and (e), or (ou), not (não), is (é).

Operadores unários:
    - not

Operadores binários:
    - and, or, is

Regras de funcionamento

Para o 'and', ambos os valores precisam ser True (verdadeiro)
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor precisa ser false (ele inverte o valor booleano, True vira False e False vira True)
Para o 'is,

"""

ativo = False
logado = True

if not logado:
    print('Conecte-se em sua conta')

if ativo and logado:
    print('Usuário ativo no sistema')

if not ativo:
    print('Você precisa ativar sua conta pelo seu email')

