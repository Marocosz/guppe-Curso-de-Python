"""
Minhas Curiosidades Gerais

Para que a saída de um for ou while seja feita toda em uma linha, utilizamos o end='' ---------------------------------

Exemplo:

while numero1 < 101:
    print(f'{numero1}', end='')
    numero1 = numero1 + 1


Pegar o último algarismo de um número e somar ==========================================================================

def somad(a):
    total = 0
    if a > 0:
        while a != 0:
            total += a % 10
            a = a // 10

        return f'A soma dos algarismo é {total}'
    else:
        return 'Número invalido'

# Exemplo com lógica condicional =======================================================================================

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)

# Exemplo com lógica condicional =======================================================================================

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)


Filtrador ==============================================================================================================

def filtrar_lista(lista):
    nova_lista = []
    for valor in lista:
        ret = None
        for letra in valor:
            try:
                ret = str(type(int(letra)))
            except:
                pass
        if not ret:
            nova_lista.append(valor)
    return nova_lista


nomes = ['miguel', 'jose', 'c5rlos']

print(filtrar_lista(nomes))


# Remover algo de string ===============================================================================================

nome = '12Marcos2'
nome = nome.strip('122')
print(nome)

# Os valores do argumento chars são removidos dos extremos inicial e final da string. Caracteres são removidos do
# extremo inicial até atingir um caractere da string que não está contido no conjunto de caracteres em chars. Uma
# ação similar acontece no extremo final da string.

# Iterando parar remover algum caracter ================================================================================

nome = 'Marcos'
exc = 'Mcs'

for x in exc:
    nome = nome.replace(x, "")

print(nome)

ou assim ===============================================================================================================

nome = 'Marcos'
exc = 'Mcs'

for x in range(len(exc)):
    nome = nome.replace(exc[x], "")

print(nome)

# Ordenar sobrenome ====================================================================================================

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card'
           , 'Douglas Admas', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

# Com isso, ordenamos a lista de acordo com o sobrenome dos autores, utilizando o [-1] para pegar o último elemento
# e ordenar com o .sort ordenar em ordem alfabética

print(autores)

# Desempacotar =========================================================================================================

dados = [(0, 1), (2, 3), (4, 5), (6, 7)]

print(*dados)  # (0, 1) (2, 3) (4, 5) (6, 7)

# Desempacotamos utilizando o '*'

# Exemplo mais complexo ================================================================================================

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carlo']

print(list(zip(alunos, prova1, prova2)))

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}  # dictionary comprehension

# É um dict com o dado[0] (Aluno) e o max entre os dado[1] e dado[2] (prova1 e prova2) para cada dado no zip

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

# Primeiro temos o zip(prova1, prova2) o qual resultará em [(80,98), (91, 89), (78, 53)]

# Utilizando o map ele pegará esse primeiro resultado e jogará no lambda que pegará o max entre cada uma dessas
# duas notas resultantes do zip

# E por último temos um zip de alunos e do resultado, quer ordernará da seguinte forma:
# {'Maria': 98, 'Pedro': 91, 'Carlo': 78}

print(dict(final))


# Função que realiza a sequência Fibonacci =============================================================================

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


ou


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


print(list(fib_gen(10)))
print(fib_lista(10))


# Formatando data ======================================================================================================

import datetime

data_a = datetime.date.today()
data_atual = ('{d}'+'/' + '{m}' + '/' + '{y}').format(d=data_a.day, m=data_a.month, y=data_a.year)
print(data_atual)
data_atual_list = data_atual.split('/')
print(data_atual_list)


# Acesso de módulos ====================================================================================================

# Podemos EXECUTAR os módulos via path, por exemplo: python Aulas\\secao_20\\testes_atividades.py
# Porém, recomendo usar todo o path, pois assim, quer dizer que ja estamos dentro do diretório 'guppe'
# Logo, recomendo: C:\Users\marco\PycharmProjects\guppe\Aulas\secao_20\testes_atividades.py

# Não importa se é '\' ou '\\'

# E para importar dentro de um arquivo py, usamos:
import Aulas.secao_20.doctests
from Aulas.secao_20 import doctests

# Usamos o '.' em vez da '\' para importar
"""

# Usando unicode =======================================================================================================

# Para usar unicode em python fazemos:
# código: U+2664

print(u'\u2664')  # Tiramos o '+' e deixamos o 'U' minúsculo
# ou
print(u'\U00002664')  # Trocamos '+' por '0000'