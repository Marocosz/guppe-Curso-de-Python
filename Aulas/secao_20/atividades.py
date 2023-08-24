def comer(comida, saudavel):

    if saudavel:
        return f'Estou comendo {comida} porque quero manter a forma'
    else:
        return f'Estou comendo {comida} porque só vivemos uma vez'


def dormir(horas):
    if horas >= 8:
        return f'Estou revigorado após dormir {horas} horas!'
    else:
        return f'Continuo cansado após dormir apenas {horas} horas'
