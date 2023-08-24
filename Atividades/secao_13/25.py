"""
Faça um programa gerenciar uma agenda de contatos. Para cada contato armazene o
nome, o telefone e o aniversário (dia e més). O programa deve permitir

(a) inserir contato
(b) remover contato
(c) pesquisar um contato pelo nome
(d) listar todos os contatos
(e) listar os contatos cujo nome inicia com uma dada letra
(1) imprimir os aniversariantes do mės.

Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados com os
dados contidos neste arquivo binário.
"""
from datetime import date

data_a = date.today()
data_atual = data_a.strftime('%d/%m/%Y')
data_atual_list = data_atual.split('/')
print(data_atual_list)

bloqueio = 0
lista_contatos = []



"""
def menu: Serve para ver se o arquivo 'contatos.txt' existe, se existir, pegará todas informações dele e transformará
em uma lista de acordo como o código lê os dados, e então excluí o arquivo 'contatos.txt' pois será salvo no final da 
mesma forma, e também serve como menu de acesso das outras funções.
"""
def menu():
    import os

    existe = os.path.exists('C:\\Users\\marco\\PycharmProjects\\guppe\\Atividades\\secao_13\\contatos.txt')
    lista = []
    lista_transicao = []
    lista_final = []

    if existe == True:
        with open('C:\\Users\\marco\\PycharmProjects\\guppe\\Atividades\\secao_13\\contatos.txt', 'r',
                  encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                for letra in linha:
                    if letra in '\n':
                        linha = linha.replace(letra, '')
                        lista.append([linha])
            for a in lista:
                for x in a:
                    x = x.split(', ')
                    lista_transicao.append(x)
            for lista in lista_transicao:
                copy = lista[2]
                lista.pop(2)
                lista_final.append([lista[0], lista[1], copy.split('/'), lista[2]])
        os.remove('C:\\Users\\marco\\PycharmProjects\\guppe\\Atividades\\secao_13\\contatos.txt')
        for lista in lista_final:
            lista_contatos.append(lista)

    print('--Menu--')
    var = input('Digite "Adicionar Contatos" para adicionar contatos\n'
                'Digite "Pesquisar Contato" para pesquisar um ou mais contatos\n'
                'Digite "Excluir Contato" para excluir um contato\n'
                'Digite "Lista" para ver sua lista de contatos\n'
                'Digite "Aniversariantes" para ver quem faz aniversário esse mês\n'
                'Digite "Sair" para salvar seus contatos e encerrar o programa\n'
                '--> ')
    if var.title() == 'Adicionar Contatos':
        adicionar()
        menu()
    if var.title() == 'Pesquisar Contato':
        pesquisa()
        menu()
    if var.title() == 'Excluir Contato':
        excluir()
        menu()
    if var.title() == 'Aniversariantes':
        aniversariantes()
        menu()
    if var.title() == 'Lista':
        if len(lista_contatos) > 0:
            for contato in lista_contatos:
                print(f'Nome: {contato[0]}\n'
                      f'Número: {contato[1]}\n'
                      f'Data de Aniversário: {contato[2]}\n'
                      f'Complemento: {contato[3]}\n')
            menu()
        else:
            print('Você não tem contatos')
            print('Para adicionar, no menu, digite "Adicionar Contatos"')
            menu()
    if var.title() == 'Sair':
        sair()



"""
def adicionar: Ela recebe 4 valores de entrada input do usuario (Nome, numero, data, complemento), essa função serve 
para moldar essas entradas e adcionalas na lista_contatos como forma de salvar os contatos adicionados e utilizando
o .sort() para deixar em ordem alfábética, e se a variavel contato for == ok, é para sair da função adicionar
"""
def adicionar():
    print('Para cancelar a operação digite "ok" na opção "Nome do Contato"')
    bloqueio_adicionar = 0
    while bloqueio_adicionar == 0:
        contato = input('Nome do Contato: ')
        if contato.title() == 'Ok':
            bloqueio_adicionar = 1
        else:
            numero = input('Número: ')
            data_de_aniversario = input('Digite a data de aniversário da pessoa:  /  /  ')
            complemento = input('Complemento (Digite "Ok" se não quiser complemento): ')
            lista_contatos.append([contato.title(), numero, data_de_aniversario.split('/'),
                                   complemento.title() if complemento.title() != "Ok" else "Sem Complemento"])
    lista_contatos.sort()


lista_procura = []

"""
def pesquisa: Recebe um valor input do usuario para saber o modo de pequisa, 'Por nome' ou 'Por letra', onde se for por
nome ira procurar o contato que está na lista_contatos com o mesmo nome dito pelo input e printa-lo

e se for 'Por letra' ira procurar todos os contatos que comece com determinada letra e printa-los
"""
def pesquisa():
    modo = input('Digite "Por Nome" se quiser pesquisar pelo nome\n'
                 'Digite "Por Letra" se quiser ver o contatos com determinada letra\n'
                 '--> ')
    if len(lista_contatos) > 0:
        if modo.title() == 'Por Nome':
            nome_pesquisa = input('Digite o nome que deseje achar: ')
            for contato in lista_contatos:
                if contato[0] == nome_pesquisa:
                    print(f'Nome: {contato[0]}\n'
                          f'Número: {contato[1]}\n'
                          f'Data de Aniversário: {contato[2]}\n'
                          f'Complemento: {contato[3]}\n')

    else:
        print('Você não tem contatos para pesquisar')

    if len(lista_contatos) > 0:
        if modo.title() == 'Por Letra':
            letra_pesquisa = input('Digite a letra que deseja procurar: ')
            for contato in lista_contatos:
                if contato[0][0] == letra_pesquisa.upper():
                    lista_procura.append(contato)
            for contato in lista_procura:
                print(f'Nome: {contato[0]}\n'
                      f'Número: {contato[1]}\n'
                      f'Data de Aniversário: {contato[2]}\n'
                      f'Complemento: {contato[3]}\n')

    else:
        print('Você não tem contatos para pesquisar')


"""
Def excluir: Recebe um valor input do usuário, um nome, que irá procurar na lista_contatos qual nome é igual ao input
e então remove-lo
"""


def excluir():
    contato_desejado = input('Digite o nome do contato que deseja remover: ')
    if len(lista_contatos) > 0:
        for contato in lista_contatos:
            if contato_desejado == contato[0]:
                lista_contatos.remove(contato)
                print(f'Nome: {contato[0]}\n'
                      f'Número: {contato[1]}\n'
                      f'Data de Aniversário: {contato[2]}\n'
                      f'Complemento: {contato[3]}\n'
                      f'Foi excluído')

    else:
        print('Você não tem contatos para excluir')


"""
Def aniversariantes: Cria uma lista de aniverariantes onde usa como entrada o índice 1 do indice 2  de cada lista dentro
da 'lista_contatos', sendo que o 'indice 2' seria a parte da data de aniversário e 'indice 1' o mês da data, e se ele
for igual ao mês atual, ele adicionará o contato na lista de aniversariantes, que será printará apenas o nome dos 
aniversariantes
"""


def aniversariantes():
    lista_aniversariantes = []
    try:
        if len(lista_contatos) > 0:
            for contato in lista_contatos:
                if contato[2][1] == data_atual_list[1]:
                    lista_aniversariantes.append(contato)
            if len(lista_aniversariantes) > 0:
                print('Os aniversariantes são:')
                for aniversariantes in lista_aniversariantes:
                    print(aniversariantes[0])

            else:
                print('Não tem Aniversariantes esse mês')

        else:
            print('Você não tem contatos')
    except:
        print('Modelo de data errado, exemplo: xx/xx/xxxx')


"""
Def sair: serve para salvar os contatos no arquivo que essa mesma função cria, 'contatos.txt' utilizando o 'open()'
com um modelo de saída dita na variável 'palavras' que pega cada dado
da lista_contatos e trnasforma em string para poder passar para um arquivo txt, assim então tendo como modelo a saída:
'Heloísa, (11) 988675423, 05/04/2004, Sem Complemento' dessa forma
"""


def sair():
    if len(lista_contatos) > 0:
        with open('contatos.txt', 'a+', encoding='utf-8') as arquivo:
            palavras = ''
            for contato in lista_contatos:
                palavras = f'{"".join(contato[0])}, {"".join(contato[1])}, {"/".join(contato[2])}, {"".join(contato[3])}'
                arquivo.write(f'{palavras}\n')
        print('Salvo e encerrando')

    else:
        print('Você não tem contatos para salvar')


menu()
