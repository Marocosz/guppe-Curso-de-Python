# Função Recursiva

# São funções que chamam a si mesmas de maneira direta ou indireta

# São úteis quando o problema pode ser dividido em problemas menores do mesmo tipo

# Caso base ===========================================================================================================

# Obrigatório ter o Caso Base, que seria a condição a qual a função ira interromper o loop, ou seja, não retorna ela
# ela mesma, e sim um valor real

# Caso Recursivo ======================================================================================================

# É a parte do código qual tem a implementação do loop do problema, onde a função a retornará ela mesma

# Exemplo:
def contagem_regressiva_recursiva(comeca_em, termina_em) -> int:
    """
    Contagem regressiva iniciando em 'comeca_em' e terminando em 'termina_em'
    """
    print(comeca_em)

    # Caso-base
    if comeca_em <= termina_em:
        # Perceba que aqui um valor real é retornado
        # e não há mais recursão
        return termina_em

    # Caso recursivo
    # Esse código será executado sempre, até
    # 'comeca_em' se tornar menor ou igual a 'termina_em'
    return contagem_regressiva_recursiva(comeca_em - 1, termina_em)


contagem_regressiva_recursiva(20, 12)

# Call Stack ==========================================================================================================

# Call Stack (Pilha de chamada) é o lugar onde é salvo os dados do seu escopo interno (variáveis e parâmetros)
# serve para saber quando a função retorna um valor para continuar o fluxo

# olhar em C:\Users\marco\Documents\PycharmProjects\guppe\Aulas\secao_08\Image_recursiva.png


