import random

# https://stringfixer.com/pt/Playing_cards_in_Unicode
from typing import Tuple, List

NAIPES: list = u'\U00002660 \U00002663 \U00002662 \U00002661'.split()
CARTAS: list = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio: bool = False) -> list[tuple[str, str]]:
    """Cria um baralho com 52 cartas para jogar"""
    baralho: list[tuple[str, str]] = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: list[tuple[str, str]]) -> tuple[
list[tuple[str, str]], list[tuple[str, str]], list[tuple[str, str]], list[tuple[str, str]]]:
    """Gerencia a mão de cartas de acordo com o baralho"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: list[tuple[str, str]] = criar_baralho(aleatorio=True)
    jogadores: list[str] = 'P1 P2 P3 P4'.split()
    maos: dict[str, list[tuple[str, str]]] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
