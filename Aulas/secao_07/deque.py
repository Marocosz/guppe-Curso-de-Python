"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance
"""

    # Importando ---------------------------------------------------------------------------------------------------

from collections import deque

    # Criando Deques --------------------------------------------------------------------------------------------------

deq = deque('Marcos')
print(deq)

    # Adicionando elementos no Deque ---------------------------------------------------------------------------------

deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('x')  # Adicona no começo
print(deq)

    # Removendo elementos no Deque ----------------------------------------------------------------------------------

print(deq.pop())  # Remove o último elemento e o retorna
print(deq)

print(deq.popleft())  # Remove o primeiro elemento e o retorna
print(deq)

