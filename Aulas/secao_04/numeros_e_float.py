"""
Tipo Numérico
"""

num = 1_000_000
print(num)

"""
Tipo Float (Decimal, real, casas decimais)

Separador de casas decimais na programação é o ponto e não a vírgula

"""
# Errado ao ponto de vista do Float, porém é gerador de uma Tupla
valor = 1, 55
print(valor)
print(type(valor))

# Correto
valor = 1.55
print(valor)
print(type(valor))

# Também é possivel:
valor1, valor2 = 1, 2
print(valor1, valor2)
print(type(valor1), type(valor2))

# Podemos converter float em int
res = int(valor)
print(res)
print(type(res))

print(float(res))
print(type(float(res)))

# Ao converter um tipo float em inteiro, perdemos precisão

"""
Para limitar os decimais aparentes podemos fazer:

num = 213.3689
print(f'{round(num, 2)}')     # Sendo o '2' a quantidade de casas que você quer

print(f'{num:.2f}     # Porém, nesse modo, mesmo se o número não tiver casas decimais, aparecerá número.00

"""

print('=================================')

num = 213

print(f'{round(num, 2)}')

print(f'{num:.2f}')
