"""
Operador Walrus

Walrus -> Permite fazer a atribuição, e retorno de valor, em uma única expressão

variável := expressão


# Normalmente ==========================================================================================================

nome = 'Marcos'
print(nome)

cesta = []
fruta = input('Informe uma fruta: ')

# ======================================================================================================================

while fruta !=  'jaca':
    cesta.append(fruta)
    fruta = input('Informe uma fruta: ')

print(cesta)
"""

# Usando Walrus ========================================================================================================

print(nome1 := 'Marcos')
print(nome1)  # E a variável existe

# ======================================================================================================================

cesta = []
while (fruta := input('Informe uma fruta: ')) != 'jaca':
    cesta.append(fruta)

print(cesta)


# OBS: Para usar type hint com walrus fazemos:

var: int
while type(var := 23) == int:
    print('Ok')

