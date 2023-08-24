"""
Recebendo os dados dos usuários

Todo dado recebido via input() é string

Em python, String é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

'Marcos'
"Marcos"
'''Marcos'''
"""
# """Marcos"""


# Entrada de Dados
# print("Qual seu nome?")
# nome = input()  # Input -> Entrada
nome = input("Qual seu nome?")

# print("Seja Bem-Vindo(a) %s" % nome)  # Forma antiga de Print
# print("Seja Bem-vindo(a) {0}" .format(nome))  # Print +- moderno
print(f"Seja Bem-vindo(a) {nome}")  # Forma mais atual de fazer print

# print("Qual a sua idade?")
# idade = input()
idade = int(input("Qual sua idade?"))

# Saída de Dados
# print("%s tem %s anos de idade!" % (nome, idade))  # Forma antiga de Print
# print("{0} tem {1} anos de idade!" .format(nome, idade))  # Print +- moderno
print(f"{nome} tem {idade} anos de idade!")  # Forma mais atual de fazer print

"""
int(idade) -> cast

cast é a conversão de um tipo de dado para outro
"""
print(f"{nome} nasceu em {2022 - (idade)}")

n = float(input())
x = 3.14159

print(f'A = {round((x*n), 4)}')