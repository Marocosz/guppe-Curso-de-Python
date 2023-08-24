"""
Em python, String é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

'Marcos'
"Marcos"
'''Marcos'''
"""
# """Marcos"""
"""
nome = 'Marcos'
print(nome)  -> Marcos
print(type(nome))

nome = "Gina's Bar"
print(nome)  -> Gina's Bar
print(type(nome))

nome = '"Marcos"'
print(nome)  -> "Marcos"
print(type(nome))

# \ é um caráctere de escape
nome = "\"Marcos\""
print(nome)  -> "Marcos"
print(type(nome))


# \n serve para pular a linha
nome = 'Marcos \nRodrigues'
print(nome)        -> Marcos
print(type(nome))     Rodrigues

nome = 'MarCos rOdriGues'
print(nome.lower())  # Transforma todos caractéres em minúsculo  -> marcos rodrigues
print(nome.upper())  # Transforma todos caractéres em maiúsculo  -> MARCOS RODRIGUES
print(nome.split())  # Transforma em uma lista de Strings  -> ['MarCos', 'rOdriGues']
print(nome.title())  # Transforma em formatação titúlo  -> Marcos Rodrigues

nome = Marcos Rodrigues
[ 'M', 'a', 'r', 'c', 'o', 's', ' ', 'R', 'o', 'd', 'r', 'i', 'g', 'u', 'e', 's']
[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15]

O python reconhece as strings dessa forma mencionada

# Slice ================================================================================================================

nome = 'Marcos Rodrigues'
print(nome[0:1])  # Slice de String
print(nome[2:9])  # Slice de String
print(nome[7:16])  # Slice de String

print('------------')

print(nome.split()[0])
# ['Marcos', 'Rodrigues']
# [    0          1     ]

print('------------')

print(nome[::-1])  # Comece do primeiro elemento, vá até o ultimo e inverta (inverter)

print(nome.replace('M', 'A'))  # Trocou a letra M por A


# Strip ================================================================================================================

nome = '   Marcos   '
nome = nome.strip()  # Serve para tirar os espaços do final e do começo 
                     # das strings, ou oque você quiser entre os parenteses
print(nome)


# Replace ==============================================================================================================

string = 'Marcos'
string = string.replace('M', 'C')
print(string)

# Replace serve para trocar um elemento da string por outro
"""

# Center ===============================================================================================================

palavra = 'Marcos'
print(palavra.center(100, '-'))

# serve para, onde o primeiro argumento é a quantidade de caracter, e o segundo qual caractere será, e o 'center' irá
# pegar a palavra colocar no meio dos 100, subtraindo a quantidade de caractere, ou seja, será 100 caracteres contando
# com a palavra
