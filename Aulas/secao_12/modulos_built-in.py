"""
Módulos Built-in

https://docs.python.org/pt-br/3/py-modindex.html

São módulos integrados, ja instalados do Python

 _______________________
/Python/Módulos Builtin/
-----------------------


# Utilizando 'alias' (apelidos) para  módulos/funções ==================================================================

import random as rdm  # com 'as rdm' definimos no código que random será rdm, assim, como no exemplo abaixo, utilizamos
                      # rdm de prefixo em vez de random, para acessar as funções

print(rdm.random())

# Podemos nomear funções também ========================================================================================

from random import randint as rdi, random as rdm

print(rdi(5, 99))
print(rdm())


# Podemos importar todas funções de um módulo utilizando o '*' =========================================================

from random import *

print(random())

# Dessa maneira não precisa do prefixo random (random.random()) apenas da função (random())


# Usando Tupple para múltiplos imports de um módulo ====================================================================

from random import (
    random,
    randint,
    shuffle,
    choice
)


"""



