"""
Unittest - Antes e Após Hooks

Hooks -> São os testes em si, ou seja, a execução dos testes

setup() ->  É executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados

tearDown -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões de banco de dados

"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Config. do setUp()
        pass

    def test_um(self):
        # setUp vai rodar antes do teste
        # TearDown vai rodar após o teste
        pass

    def test_dois(self):
        # setUp vai rodar antes do teste
        # TearDown vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass

