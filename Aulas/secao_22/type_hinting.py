"""
Type Hinting - Dicas de Tipos

É de extrema importância o uso do Type Hinting

# Vantagens:
    - Facilita achar erros do código
    - Melhor documentação
    - Ajuda a IDE com os completes

# Desvantagens:
    - Código um pouco mais lento



# Usando Type Hinting ==================================================================================================


def cumprimentar(nome: str, numero: int, ) -> str:
    return f'Olá,{nome}, {numero}'


# Isso seria o 'Type Hinting', utilizando ': str' para indicar que tipo de dado de entrada será, e ' -> str' como tipo
# de dado da saída

print(cumprimentar('Marcos', 2))


def cabecalho(texto: str = 'Cabeçalho', alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f'{texto.title()}'.center(20, '#')


print(cabecalho())
print(cabecalho(alinhamento=False))
print(cabecalho('Marcos', True))

# Caso seja um parâmetro não opcional, podemos colocar o '= valor' na frente da definição de tipo, como na função acima

a: str = 'as'  # Também há como definir em variáveis fora da função
b: int = 123


# Annotations ==========================================================================================================

# Podemos saber as referências, anotações, usando:

print(cabecalho.__annotations__)  # {'texto': <class 'str'>, 'alinhamento': <class 'bool'>, 'return': <class 'str'>}
print(__annotations__)  # {'a': <class 'str'>, 'b': <class 'int'>} Pegamos as variáveis do código:
"""

# Usando no POO ========================================================================================================


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome}, está andando!'


p = Pessoa(nome='Marcos', idade=18, peso=62.5)

print(p.__dict__)

# print(p.__annotations__)  # Não existe!

print(p.__init__.__annotations__)  # Usamos dessa forma
# {'nome': <class 'str'>, 'idade': <class 'int'>, 'peso': <class 'float'>, 'return': None}

lista: list[list[tuple[int, int]]] = [[(1, 2)]]