def conta(a, b, alg):
    if alg == '+':
        return a + b
    elif alg == '-':
        return a - b
    elif alg == '*':
        return a * b
    elif alg == '/':
        return a/b


print(conta(5, 10, '+'))