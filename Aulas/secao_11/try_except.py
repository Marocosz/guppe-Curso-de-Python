"""
O bloco Try/Except

Usamos ele para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar
e o utilizador não receba mensagens de erro inesperada

A Forma geral mais simples:

try:
    # Execução problemática
excepet:
    # O que deve ser feito em caso de problema


# Exemplo Genêrico =====================================================================================================

try:
    marcos()

except:
    print('Deu algum problema')

# Tente executar a função 'marcos()', caso encontre erro, imprima a mensagem definida

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento. O ideal é sempre tratar de
forma específica


# Exemplo Específico ===================================================================================================

try:
    marcos()

except NameError:  # Definiu o possivel problema, se não for esse tipo de erro, havera erro no código
    print('Voce está utilizando uma função inexistente')


# Exemplo Com Detalhe ==================================================================================================

try:
    len(5)

except TypeError as erro:
    print(f'A aplicação gerou o seguinte erro: {erro}')


# Exemplo Com mais de um erro ==========================================================================================

try:
    print('Marcos'[203])

except NameError as erroa:
    print(f'Deu NameError: {erroa}')

except TypeError as errob:
    print(f'Deu TypeError: {errob}')

except:
    print('Houve um erro diferente')


# Exemplo com Função ===================================================================================================




"""
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]

    except KeyError:
        return None
    except TypeError:
        return None
    except:
        return None


dic = {'nome': 'Marcos'}

print(pega_valor(dic, 'sobrenome'))




