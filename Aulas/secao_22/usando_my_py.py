"""
MyPy  (pip install mypy)

MyPy -> Serve para checar tipos de dados de variáveis caso esteja errado nos argumentos dados

"""


def cabecalho(texto: str = 'Cabeçalho', alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f'{texto.title()}'.center(20, '#')


print(cabecalho())
print(cabecalho(alinhamento=False))
print(cabecalho('Marcos', 'as'))  # Aviso sobre não estar recebendo o tipo de dado devido


# Para usar vá no terminal e escreva: mypy C:\Users\marco\PycharmProjects\guppe\Aulas\secao_22\usando_my_py.py

