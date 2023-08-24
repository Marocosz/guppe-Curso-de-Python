# numeros primos
numbers = int(input())
lista_numeros = []

for x in range(1, numbers + 1):
    lista_numeros.append(x)


lista_primos = []

for number in range(1, numbers + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            lista_primos.append(number)

for primo in lista_primos:
    if primo < len(lista_numeros):
        print(primo)

print(lista_numeros)