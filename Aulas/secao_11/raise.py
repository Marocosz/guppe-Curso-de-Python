"""
Levantando próprios erros com raise

Raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou outras

Para simplificar pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro

# Forma geral de utilização:

raise TipoDoErro('Mensagem de erro')

# Exemplo ==============================================================================================================


def colore(texto, cor):

    cores = ('verde', 'amarelo', 'azul', 'branco', 'preto')

    if type(texto) is not str:
        raise TypeError('"texto" precisa ser uma string')

    if type(cor) is not str:
        raise TypeError('"cor" precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores!r}')

    print(f'O texto: {texto}, será impresso na cor: {cor}')


# OBS: Usamos '!r' para deixarmos entre aspas quando notificar por exemplo:
# ValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco', 'preto')
# 'Verde', 'amarelo',... Dessa forma

colore(True, 1)  # Erro
colore('marcos', 'Marrom')  # Erro

"""
