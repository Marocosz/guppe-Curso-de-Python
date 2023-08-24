def hora(h, m, s):
    hs = h * 3600
    ms = m * 60
    total = hs + ms + s
    return f'A conversão para segundos é {total} segundos'

print(hora(3, 12, 25))
