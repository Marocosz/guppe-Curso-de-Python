"""
Escrevendo um iterator customizado

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


cont = Contador(1, 4)

print(cont.menor)
print(cont.maior)

it = iter(cont)

print(next(it))
print(next(it))
print(next(it))

for n in Contador(1, 11):
    print(n)


# Dessa forma replicamos uma parte do range, utilizando o dunder iter e o dunder next transformamos
# a classe em um iterável