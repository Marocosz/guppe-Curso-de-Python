print('Digite os dois números que queira conferir:')
num1 = float(input())
num2 = float(input())
nump = 0
numr = 0

if num1 > num2:
    print(f'O maior numero é {num1}')
    nump = num1
    numr = num2
else:
    print(f'O maior numero é {num2}')
    nump = num2
    numr = num1

print(f'E a diferença entre eles é {nump - numr}')

