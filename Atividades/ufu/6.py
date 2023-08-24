nota = float(input("Digite sua nota: "))

if nota >= 5.0:
    print("Nota azul, parabéns")
    formado = input("Você é formado? Sim ou não:")
    if formado.title() == "Sim":
        print("Sucesso!")
    else:
        print("Continue firme")
else:
    cursou = int(input("Você já havia cursado a discplina anteriormente? Se sim, quantas vezes, se não, digite 0:"))
    if cursou >= 1:
        print("Nota vermelha, cuidado com o risco de jubilamento!")
        print("Precisa estudar mais, não desanime!")
    else:
        print("Nota vermelha, estude mais e não desanime!")


print("Seja Feliz!")