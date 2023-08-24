a=int(input("Insira o valor do numerador da fração\n"))
b=int(input("Insira o valor do denominador da fração\n"))


def simplifica(a, b):
    maior_denominador = 1
    for x in range(1, a + b):
        if a % x == 0 and b % x == 0:
            maior_denominador = x

    return print(f"{int(a / maior_denominador)} / {int(b / maior_denominador)}")


simplifica(a, b)