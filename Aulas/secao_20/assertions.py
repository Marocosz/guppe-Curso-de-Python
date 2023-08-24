"""
# MELHOR USAR 'TRY/EXCEPT' OU 'RAISE' PARA TESTAR ERROS DE CÓDIGOS

Assertions (Afirmações/Checagens/Questionamentos)

Em Python usamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão se queremos checar se é válida ou não
Se a expressão for verdadeira, o assert retorna 'None', caso seja false, levanta um erro do tipo 'AssertionError'

OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso, não necessariamente nos códigos testes

ATENÇÃO! Se um programa Python for executado com o parâmetro -O, nenhum assertion será validada, ou seja, todas
suas validações não servirão, como se não existissem


"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


# print(soma_numeros_positivos(2, 4))
# print(soma_numeros_positivos(-2, 4))  # AssertionError: Ambos números precisam ser positivos


def comer_fast_food(comida):
    assert comida in ['pizza', 'sorvete', 'hamburguer', 'cachorro quente'], 'A comida precisa ser fast food'
    return f'Estou comendo {comida}'


# print(comer_fast_food('pizza'))  # Estou comendo pizza
# print(comer_fast_food('arroz'))  # AssertionError: A comida precisa ser fast food

