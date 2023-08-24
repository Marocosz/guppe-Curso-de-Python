"""
PEP = Python Enhacement Proposal

E a ideia do PEP8 é que possamos escrever códigos Pyhton de forma Pythônica, ou seja,
da forma bonita, leve, explícita.

[1]- Utilize Camel Case para nomes de classe;

    class Calculadora:
        pass


    class CalculdoraCientifica:
         pass

[2]- Utilize nomes em minúsculo e separados por underline para funções ou variáveis;

    def soma():
        pass


    def soma_dois():
        pass

    numero = 4

    numero_impar = 5

[3]- Utilize 4 espaços para identação!!!!!!!!!!!! ---------------------------

    -Não usar o TAB

[4]- Linhas em Branco

    - Separar funções e definições de classe com duas linhas em branco
    - Metódos dentro de uma classe devem ser separados por uma única linha em branco

[5]- Imports

    -Imports devem ser sempre feitos em linhas separadas

    # Import Errado

    import sys, os

    # Import Correto

    import sys
    import os

    # Não tem problemas ao utilizar:

    from types import StringType, ListType

    # Mas para casos onde queira muitos imports de um pacote, é recomendado:

    from types import (
        StringType
        ListType
        SetType
        OutroType
    )

    # Imports devem ser colocados no topo do código, logo depois de
    qualquer comentario ou docstringse antes de constantes ou variaveis globais.

[6]- Espaços em expressões e instruções

    # Não faça:

    função( algo[ 1 ], { outro: 2 } )

    # Faça:

    função(algo[1], {outro: 2})

    # Não faça:

    algo (1)

    # Faça:

    algo(1)

    # Não faça:

    dict ['chave'] = lista [indice]

    # Faça:

    dict['chave'] = lista[indice]

    # Não faça:

    x              = 3
    y              = 2
    variavel_longa = 6

    # Faça:

    x = 3
    y = 2
    variavel_longa = 6

[7]- Termine sempre uma instrução com uma nova linha
"""