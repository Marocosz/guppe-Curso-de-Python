var39_i = int(input('Valor para o triangulo de pascal: '))
var39 = list()
for a in range(var39_i):
    if len(var39) < 2:
        var39.append(1)
    elif len(var39) >= 2:
        for b in range(len(var39) - 1):
            var39.append(var39[b] + var39[b + 1])
        for c in range(len(var39) - a):
            var39.pop(1)
        var39.append(1)
    print(var39)