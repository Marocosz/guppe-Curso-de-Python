cont = 0

lista = []

while cont < 3:
    x = float(input("Digite seu valor: "))
    lista.append(x)
    cont = cont + 1

print(f"Os itens adicionados foram em ordem (x,y,z): {lista}")