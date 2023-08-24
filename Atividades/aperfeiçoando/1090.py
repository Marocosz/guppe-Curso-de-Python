qtd = int(input())

if qtd >= 3:
    cartas = []
    cartas_separadas = []

    um_quadrado = 0
    dois_quadrado = 0
    tres_quadrado = 0

    um_bolinha = 0
    dois_bolinha = 0
    tres_bolinha = 0

    um_triangulo = 0
    dois_triangulo = 0
    tres_triangulo = 0

    sets = 0

    for x in range(qtd):
        nome_carta = input()
        cartas.append(nome_carta)

    for carta in cartas:
        y = carta.split()
        cartas_separadas.append(y)

    for h in cartas_separadas:
        if h[0].lower() == "um":
            if h[1].lower() == "quadrado":
                um_quadrado += 1

            elif h[1].lower() == "circulo":
                um_bolinha += 1

            elif h[1].lower() == "triangulo":
                um_triangulo += 1

        if h[0].lower() == "dois":
            if h[1].lower() == "quadrados":
                dois_quadrado += 1

            elif h[1].lower() == "circulos":
                dois_bolinha += 1

            elif h[1].lower() == "triangulos":
                dois_triangulo += 1

        if h[0].lower() == "tres":
            if h[1].lower() == "quadrado":
                tres_quadrado += 1

            elif h[1].lower() == "circulos":
                tres_bolinha += 1

            elif h[1].lower() == "triangulo":
                tres_triangulo += 1

    # ========================================================================================================

    for i in range(um_quadrado):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(dois_quadrado):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(tres_quadrado):
        if (i + 1) % 3 == 0:
            sets += 1

    # ========================================================================================================

    for i in range(um_triangulo):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(dois_triangulo):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(tres_triangulo):
        if (i + 1) % 3 == 0:
            sets += 1

    # ========================================================================================================

    for i in range(um_bolinha):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(dois_bolinha):
        if (i + 1) % 3 == 0:
            sets += 1

    for i in range(tres_bolinha):
        if (i + 1) % 3 == 0:
            sets += 1

    # ========================================================================================================

    if tres_quadrado >= dois_triangulo:
        if dois_triangulo >= um_bolinha:
            for x in range(um_bolinha):
                sets += 1

    elif tres_quadrado >= um_bolinha:
        for x in range(um_bolinha):
            sets += 1

    elif tres_quadrado <= um_bolinha:
        for x in range(tres_quadrado):
            sets += 1

    else:
        for x in range(dois_triangulo):
            sets += 1

    # ========================================================================================================

    if dois_quadrado >= um_triangulo:
        if um_triangulo >= tres_bolinha:
            for x in range(tres_bolinha):
                sets += 1

    elif dois_quadrado >= tres_bolinha:
        for x in range(tres_bolinha):
            sets += 1

    elif dois_quadrado <= tres_bolinha:
        for x in range(dois_quadrado):
            sets += 1

    else:
        for x in range(um_triangulo):
            sets += 1

    # ========================================================================================================

    if um_quadrado >= tres_triangulo:
        if tres_triangulo >= dois_bolinha:
            for x in range(dois_bolinha):
                sets += 1

    elif um_quadrado >= dois_bolinha:
        for x in range(dois_bolinha):
            sets += 1

    elif um_quadrado <= dois_bolinha:
        for x in range(um_quadrado):
            sets += 1

    else:
        for x in range(tres_triangulo):
            sets += 1

    print(sets)