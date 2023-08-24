comprimento = float(input('Comprimento do terreno:'))
largura = float(input('Largura do terrreno:'))
tela = float(input('Preço por metro da tela'))

resultado = ((comprimento * 2) + (largura * 2)) * tela
print(f'O custo será de {resultado} reais.')
