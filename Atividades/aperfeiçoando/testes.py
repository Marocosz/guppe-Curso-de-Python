frase: str = input("Digite a sentença que deseja transformar: ")
frase: str = frase.lower()

cont: int = len(frase)

for x in range(cont):
    if x % 2 == 0:
        frase = ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(frase))


print(frase)