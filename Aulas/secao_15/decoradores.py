"""
Decoradores (Decorators)

O que são:

- Decorators são funções.
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators são exemplos de HOF
- Decorator tem uma sintaxe própria, usando '@' (Syntact Sugar / Açúcar sintático)


- De modo geral, decorators são funcionalidades que irão implementar outras funções, irá pegar X função como parâmetro,
  e então de acordo com o que você quiser, rodará essa função adjunto ao decorator, se o decorator quiser printar ou
  fazer algo especifico, ele fará ao rodar a função

OBS: Não usar 'return' na decorator wrapper

Decorator wrapper -> A função que terá a funcionalidade desejada
"""
# Decorator com Syntact Sugar (Açucar sintático) =======================================================================

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo


@seja_educado
def apresentando():
    print('Meu nome é Marcos')


apresentando()
# Dessa forma, decoramos a função 'apresentando()' fazendo com que ela vire a variavel 'funcao' que está dentro de
# 'seja_educado'

# Exemplo ==============================================================================================================


def teste(funcao):
    def testado(a):
        if funcao(a) != 10:
            print('Diferente de 10')
            print(a)
        else:
            print('Igual a 10')
            print(a)
    return testado


@teste
def numero(a):
    return a


numero(10)  # Igual a 10

"""
# Exemplo 2 ============================================================================================================

logado = False


def check():
    if not logado:
        print('Logue para acessar essa parte')


@check
def entrar():
    print('Entrou')


entrar()
"""



