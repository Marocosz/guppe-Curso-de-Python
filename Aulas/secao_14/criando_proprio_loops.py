# Criando sua própria versão de loop

# loops:

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Marcos':
    print(letra)


# Dessa forma fazemos um loop igual ao loop 'for' integrado da linguagem ===============================================


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Marcos')
meu_for([1, 2, 3, 4, 5])

