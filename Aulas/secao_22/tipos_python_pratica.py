"""
Aplicando tipos de dados em Python na prática

"""
# Dados mais complexos =================================================================================================

nomes: list[str] = ['Marcos', 'Rodrigues']
versoes: tuple[int, int, int] = (1, 2, 3)
opcoes: dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: set[int] = {1, 2, 3, 4}

print(__annotations__)
# {'nomes': list[str], 'versoes': tuple[int, int, int], 'opcoes': dict[str, bool], 'valores': set[int]}



