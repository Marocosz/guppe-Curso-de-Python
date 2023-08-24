sal = float(input('Qual seu salário?'))
emp = float(input('Qual o valor de empréstimo'))

salc = sal * 0.2

if emp > salc:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
