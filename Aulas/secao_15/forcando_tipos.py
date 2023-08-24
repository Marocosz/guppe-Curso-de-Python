"""
Forçando tipos de dados com decoradores


"""

# Conversor de tipos de variáveis ======================================================================================


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Marcos'), int('2')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, rep):
    for vez in range(rep):
        print(msg)


repete_msg('Marcos', '2')

# Dessa forma, mesmo se passarmos uma string, será contabilizado como um int, pois foi convertido pelo decorator

