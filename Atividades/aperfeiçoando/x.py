# cria uma matriz 3x3 para representar o tabuleiro do jogo da velha
tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# define a função que desenha o tabuleiro do jogo
def desenhar_tabuleiro():
    print('   0  1  2')
    for i in range(3):
        print(i, ' ', end='')
        for j in range(3):
            if j < 2:
                print(tabuleiro[i][j], '|', ' ', end='')
            else:
                print(tabuleiro[i][j])

# define a função que verifica se um jogador venceu o jogo
def verificar_vitoria(jogador):
    # verifica se alguma linha está completa
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True

    # verifica se alguma coluna está completa
    for j in range(3):
        if tabuleiro[0][j] == jogador and tabuleiro[1][j] == jogador and tabuleiro[2][j] == jogador:
            return True

    # verifica se alguma diagonal está completa
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

# define a função que verifica se o jogo terminou
def verificar_fim_de_jogo():
    # verifica se o tabuleiro está completo
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

# define a função que permite um jogador fazer uma jogada
def jogar(jogador):
    linha = int(input('Digite a linha da sua jogada (0, 1 ou 2): '))
    coluna = int(input('Digite a coluna da sua jogada (0, 1 ou 2): '))
    if tabuleiro[linha][coluna] != ' ':
        print('Essa posição já está ocupada. Tente novamente.')
        jogar(jogador)
    else:
        tabuleiro[linha][coluna] = jogador

# define as variáveis que representam os jogadores
jogador1 = 'X'
jogador2 = 'O'

# define a variável que representa o jogador atual
jogador_atual = jogador1

# inicia o jogo
while True:
    # desenha o tabuleiro do jogo
    desenhar_tabuleiro()

    # pede para o jogador atual fazer uma jogada
    print('Vez do jogador', jogador_atual)
    jogar(jogador_atual)

    # verifica se o jogador atual venceu o jogo
    if verificar_vitoria(jogador_atual):
        print('Jogador', jogador_atual, 'venceu o jogo!')
        desenhar_tabuleiro()
        break

    # verifica se o jogo terminou empatado
    if verificar_fim_de_jogo():
        print('O jogo terminou empat')