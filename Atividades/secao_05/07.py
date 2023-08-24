print('Digite os dois números que queira conferir:')
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print(f'O maior número é {num1}')
elif num1 == num2:
    print('Os números são iguais')
else:
    print(f'O maior número é {num2}')
