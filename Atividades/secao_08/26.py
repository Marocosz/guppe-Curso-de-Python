num = int(input('Digite até que número deseja somar'))


def soma(x):
    soma = 0
    for num in range(1, x + 1):
        soma = soma + num

    return f'A soma até seu número é {soma}'


print(soma(num))