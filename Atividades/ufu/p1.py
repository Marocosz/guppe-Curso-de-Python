n = int(input("Digite a quantidade de números a serem lidos: "))

if n <= 4:
    while n >= 1:
        x = int(input("Digite o Valor: "))
        print(f"Valor: {x}")
        n = n - 1
else:
    print("cansei de trabalhar!")