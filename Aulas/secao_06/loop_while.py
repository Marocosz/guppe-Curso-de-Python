"""
Loop While

Forma Geral:

while expressão_booleana:
    //execução do loop

O bloco do while será repeitdo enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplos:

num = 5
num < 5 -> False

# OBS: Em um loop while é importante que cuidemos do critério de parada, para não tornar um loop infinito
"""
numero = 1

# Exemplo 01
while numero <= 10:
    print(numero)
    numero = numero + 1

resposta = ''


while resposta != 'Sim':
    resposta = input('Você é gay?')
    resposta = resposta.title()

