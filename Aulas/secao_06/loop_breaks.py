"""
Saindo de loops com break

Utilizamos o break para encerrar loops de maneira forçada
"""

# Exemplo 01:
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)

print('Saiu do loop')

# Exemplo 02:
while True:
    comando = input('Digite "Sair" para sair')
    comando = comando.title()
    if comando == 'Sair':
        break
    print(comando)