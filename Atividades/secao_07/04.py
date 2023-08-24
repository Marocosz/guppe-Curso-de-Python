contador = 0
vetor = []
soma = []
while contador < 8:
    valor = int(input(f"Digite o valor da {contador + 1}º posição do vetor:\n"))
    contador += 1
    vetor.append(valor)
posicao_X = int(input("Coloque um valor X compátível com o tamanho da lista:"))
posicao_Y = int(input("Coloque um valor Y compátível com o tamanho da lista:"))
if 0 < posicao_X <= len(vetor) and 0 < posicao_Y <= len(vetor):
    soma = [vetor[posicao_X - 1], vetor[posicao_Y - 1]]
    print(f"A soma dos valores encontrados nas posições {posicao_X} e {posicao_Y} é: {sum(soma)}")
else:
    print("As posições desejadas precisam ser compatíveis com o tamanho da lista !")