"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo no modo leitura, apenas podemos ler, não escrever e ao abrir em modo escrita,
podemos apenas escrever, não ler

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

# Usamos a função write(string) para escrever dentro do txt

# OBS: Abrindo um arquivo para escrita no modo 'w', se o arquivo não existir, será criado, caso exista,
o anterior será apagado e um novo será criado. Dessa forma todo conteudo do arquivo anterior é apagado
e o novo conteúdo colocado

# Exemplo ==============================================================================================================

# Utilizamos 'w' para abrir no modo escrita, por padrão é 'r', modo leitura

with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito Fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos. \n')
    arquivo.write('É muito fácil utilizar. \n')
    arquivo.write('E também é muito útil, e esta é a última linha')


# Podemos usar as funções de string para escrever ======================================================================

with open('mais.txt', 'w', encoding='utf-8') as arquivo2:
    arquivo2.write('Marcos\n' * 1000)
"""

# Comunicando com o usuario ============================================================================================

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break