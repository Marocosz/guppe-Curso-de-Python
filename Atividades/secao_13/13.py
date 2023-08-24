"""
Faça um programa que permita que o usuario entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informaçoes, uma por linha. O usuario finaliza a
entrada com '0' para o telefone.
"""
print('Digite as informações e para finalizar digite "0"')

with open('lista_contato', 'a+', encoding='utf-8') as arquivo:
    while True:
        numero = input('Digite o número da pessoa: ')
        if numero == '0':
            arquivo.seek(0)
            print(arquivo.read())
            break
        for x in numero:
            if x not in '1234567890':
                print('Número invalido')
                bloqueio = 0
            else:
                bloqueio = 1
        if bloqueio == 1:
            nome = input('Digite o nome da pessoa: ')
            arquivo.write(f'{nome}: {numero}\n')
