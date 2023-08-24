"""
Para lidarmos com o problema do GIL de python, podemos em vez de utilizar multi_threads, usarmos mult_processing

# Vemos que usando multi_processing o tempo de execução do código foi bem mais rápido que single ou multi threads

Porém multi_processing são mais 'pesados'
"""

from multiprocessing import Pool
import time

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//2])
    r2 = pool.apply_async(contagem_regressiva, [contador//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos: {fim - inicio}')  # Tempo em segundos: 1.519148826599121

