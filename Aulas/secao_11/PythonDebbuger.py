"""
Debuggando com PDB (Python Debbuger)


# Exemplo PyCharm ======================================================================================================

# Clique do lado da linha que deseja analisar e então clique no debbug, podendo jogar no 'watch' determinada função
# Para receber o resultado dela

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError, ValueError) as erro:
        return f'Ocorreu o erro: {erro}'


print(dividir(4, 0))


# Exemplo PDB 1 ========================================================================================================

# Primeiramente temos que importar ele da biblioteca pdb e usar a função set_trace()

# Comandos:

# l -> Listar onde estamos no código
# n -> Próxima linha
# p -> Imprimi Variável
# c -> Continua a execução / Finaliza o debugging

import pdb

nome = 'Marcos'
sobrenome = 'Rodrigues'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' Faz o curso' + ' ' + curso
print(final)

# Exemplo PDB 2 ========================================================================================================


nome = 'Marcos'
sobrenome = 'Rodrigues'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' Faz o curso' + ' ' + curso
print(final)

# Por que utilizar dessa forma?
# O debbug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de biblioteca
# no ínicio do arquivo

# dessa forma, como o debbug é apenas pra resolução de problemas, colocamos o import junto para excluir depois


# OBS: A partir do python 3.7 não precisamos mais importar, utilizamos o breakpoint() que está integrado na linguagem


# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos pdb ================================================

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 2, 3, 4))


# Se houver variáveis igual os comandos pdb, devemos utilizar o comando 'p' para imprimir ou seja:
# p 'variavel'

# Porém é muito melhor que coloque nomes representativos em variáveis
"""



