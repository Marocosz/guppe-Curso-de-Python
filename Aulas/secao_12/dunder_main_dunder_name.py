"""
Dunder Main e Dunder Name

dunde = Double Under '__'

Dunder Main  -> __main__
Dunder Name -> __name__

Em Python, são utilizados dunder para criar funções, atributos/propriedades e etc, serve para não gerar
conflito com os nomes desses elementos na programação


# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuíra à variável __name__ o valor __main__ indicando que este módulo é o módulo
de execução principal


# __name__ e __main__ é utilizado geralmente para testes de módulo, pois se houver prints ou execuções de
tarefas/funções em um arquivo e esse arquivo está sendo importado para outro, essas mesmas tarefas sendo feitas nele
será executada no arquivo que importou. Sendo assim então utilizando:

if __name__ == '__main__':
    'execução'

serve para que isso não aconteça e possamos fazer os testes dentro do módulo que será importado

"""

