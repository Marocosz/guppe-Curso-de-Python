"""
1. Escreva um programa que:

(a) Crie/abra um arquivo texto de nome "arq.bxt"

(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuario
entre como caractere 0'

(c) Feche o arquivo

Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.
"""

with open('arq', 'w', encoding='utf-8') as arq:
    print('Digite oque deseja e finalize escrevendo "0"')
    while True:
        x = input()
        if x != '0':
            arq.write(f'{x}\n')
        else:
            break

with open('arq', 'r', encoding='utf-8') as arq:
    arq.seek(0)
    print(f'O que você escreveu foi:\n\n{arq.read()}')
