"""
Tipos de dados que são mais Precisos

Tipos de dados: str, int, float, bool, bin, List, Dict...

Tipos de dados mais precisos: Literal type, Union, Final, Typed dictionaries, Protocols


# Literal type =========================================================================================================

from typing import Literal

# Literal significa que a variável, o retorno, é um valor absoluto, se literal é = 'desconectado', ele é 'desconectado'
# não uma string


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


# Por exemplo, na função acima: Ele espera retornar literalmente 'conectado' ou 'desconectado' e nada mais


# Sem 'Literal type' ===================================================================================================

from typing import Literal


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # '!r' para deixar oque tiver em 'operação' entre aspas


calcula_v1('+', 2, 5)
calcula_v1('-', 10, 5)
calcula_v1('*', 20, 2) # ValueError: Operação inválida '*'


# Usando 'Literal type' ================================================================================================

from typing import Literal


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # '!r' para deixar oque tiver em 'operação' entre aspas


calcula_v2('+', 2, 5)
calcula_v2('-', 10, 5)
calcula_v2('*', 20, 2) # ValueError: Operação inválida '*'

# OBS: Com o 'Literal Type' definimos de forma absoluta oque queremos de argumento no parâmetro 'operacao'
# Usando o mypy vemos o seguinte error:
# Argument 1 to "calcula_v2" has incompatible type "Literal['*']"; expected "Literal['+', '-']"


# Union ================================================================================================================

from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'{resultado} é um valor muito alto'
    else:
        return resultado


print(soma(10, 2))  # 12  -  Um int
print(soma(213, 2))  # 215 é um valor muito alto  -  Uma str

# Ou seja, o 'Union' serve para especificar mais de um tipo de dado que queremos ter como return, ou como argumento


# Final ================================================================================================================

from typing import Final

# O 'Final' serve pra criar constantes, ou seja, que não podem alterar o valor, porém no Python, não há problemas,
# mas quando usar o mypy se houver a modificação, haverá error

NOME: Final = 'Marcos'

print(NOME)


# Decorador Final ======================================================================================================

from typing import final

# O decorador final, serve para indicar que determinada função não pode ser sobrescrita, ou que determinada class
# não pode ser uma super class


@final  # Ou seja, a class Pessoa, com o @final, não pode ser usada como super class
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e trabalhando')


# Typed dictionaries ===================================================================================================

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.10.1', atualizacao=2022)

print(geek)  # {'versao': '3.10.1', 'atualizacao': 2022}

# Usamos 'TypedDict' como uma superclass, que serve para criar um dictionare de acordo com as variáveis da class
"""

# Protocols ============================================================================================================

from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Aprenda a vender'


v1 = Venda()
print(v1.titulo)
estudar(v1)


# Criamos uma class com a superclass 'Protocol' tornando essa class um protocolo, que quer dizer que, todos os objetos
# de outras class tiver o seguinte protocolo ( no caso do 'Curso', for igual a ela, ou seja, ter a variavel titulo),
# será uma classe 'Curso', sendo assim, poderá usar a função que pede um valor 'Curso', e as classes protocolo
# não podem ser instanciadas


