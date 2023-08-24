import math

def volume_esfera(r):
    return round(4/3 * math.pi * (r**3), 2)

print(volume_esfera(10))