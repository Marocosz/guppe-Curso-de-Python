"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas
- Pode ou não entrar dados ou sair dados
- Muito úteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom
fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções, por exemplo:
    -print()
    -len()
    -max()
    -min()
    -count()
    -várias outras...


    # Exemplo de utilização de Funções --------------------------------------------------------------------------------

cores = ['verde', 'amarelo', 'azul', 'branco']

    # Utilizando uma função integrada (Bult-in) do python

print(cores)

cores.append('roxo')

# Dry - Don't Repeat Yourself - Não repeita você mesmo


    # Definir a funçãa ---------------------------------------------------------------------------------------------

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função

Onde:

nome_da_funçao -> SEMPRE com letras minúsculas e se for composto utilizar _ (Snake Case)

parâmetros_de_entrada -> Opicionais, e se houver mais de um, separar por vírgula

bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função
acontece. Neste bloco pode ter ou não o retorno da função

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código já conhecido ':'


    # Definindo a primeira função ----------------------------------------------------------------------------------

def diz_oi():
    print('OI!!')


# OBS: Veja que dentro de nossas funções podemos utilizar outras funções
# OBS: Essa função não recebe nenhum parâmetro de entrada
# OBS: Ela também não retorna nada

    # Chamando a função ---------------------------------------------------------------------------------------------

diz_oi()

# Atenção com os parênteses'()'


def cantar_parabens():
    print('Parabés pra você \nNessa data querida \nMuitas felicidades \nE muitos anos de vida')

for n in range(5):
    cantar_parabens()

"""

def cantar_parabens():
    print('Parabés pra você \nNessa data querida \nMuitas felicidades \nE muitos anos de vida')
