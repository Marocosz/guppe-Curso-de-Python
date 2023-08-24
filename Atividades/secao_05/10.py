alt = float(input('Qual sua altura?'))
gen1 = input('Qual seu sexo?')

gen = gen1.title()

if gen == 'Feminino':
    calc1 = (62.1 * alt) - 44.7
    print(f'Seu peso ideal é {round(calc1, 2)}')

if gen.title() == 'Masculino':
    calc2 = (72.7 * alt) - 58
    print(f'Seu peso ideal é {round(calc2, 2)}')
