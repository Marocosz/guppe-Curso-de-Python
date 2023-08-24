"""
Thread é a tarefa que um determinado programa realiza. Fio de execução, também conhecido como linha ou
encadeamento de execução, é uma forma de um processo dividir a si mesmo em duas ou mais tarefas que podem ser
executadas concorrencialmente

E no python, apenas é executado 1 thread por vez, por conta do GIL - Python Global Interpreter Lock
"""


import time
from threading import Thread

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')  # Tempo em segundos: 2.9730467796325684