"""
Módulo Random

- Em Python, módulo nada maissão do que outros arquivos Python

Módulo Random -> Possui várias funções oara geração de números pseudoaleatórios

========================================================================================================================

# OBS: Podemos ver as funções dentro de um pacote utilizando 'dir', por exemplo: dir(random)
# OBS: E utilizar o 'help' para abrir a documentação, por exemplo: help(random.random)

========================================================================================================================

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 01 - Importando todo o módulo ==================================================================================
# (Não recomendado)

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedade que estiverem
# Dentro do módulo ficarão dispóniveis, em memória.


# Forma 02 - Importanto Especificamente ================================================================================
# (Forma recomendada)

from random import random

# Ou seja: Do pacote random, importe a função random
# Assim importamos apenas uma função do pacote, diminuindo a memória utilizada

for i in range(10):
    print(random())

# Importando dessa forma, não há mais necessidade de escrever 'random.random()'


# Função Random ========================================================================================================

# random() -> Gera um número real pseudoaleatório entre 0 e 1

import random

print(random.random())

# Veja que parar utilizar a função random() do pacote random, nós colocamos o nome do pacote eo nome da função
# Separados por ponto


# Função Uniform =======================================================================================================

# uniform() -> Gera um número real pseudoaleatório entre valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # Gera valores aleatórios entre 3 e 7


# Função randint =======================================================================================================

# randint() -> Gera números inteiros pseudoaleatórios entre valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # Começa em 1, e vai até 60


# Função Choice ========================================================================================================

# choice() -> Mostra um valor aleatório entre um iterável.

jogadas = ['Pedra', 'Papel', 'Tesoura']

from random import choice

print(choice(jogadas))



"""

# Função Shuffle =======================================================================================================

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '1', '2', '3', '4', '5', '6']

print(cartas)

shuffle(cartas)

print(cartas.pop())

