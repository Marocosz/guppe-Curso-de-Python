import unittest

from atividades import comer, dormir  # Importando as funções do módulo 'atividades' criado por nós


class AtividadesTestes(unittest.TestCase):  # Class de teste do módulo 'unittest'

    # Test Case

    def test_comer_saudavel(self):  # Colocamos 'test_' na frente do nome da função que estamos testando para nomear essa função
        """Testando o retorno com comida saudável"""
        self.assertEqual(comer('quiabo', True), f'Estou comendo quiabo porque quero manter a forma')

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(comer(comida='pizza', saudavel=False), 'Estou comendo pizza porque só vivemos uma vez')

    def test_dormindo_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(dormir(4), 'Continuo cansado após dormir apenas 4 horas')

    def test_dormindo_muito(self):
        self.assertEqual(dormir(9), 'Estou revigorado após dormir 9 horas!')

        # Vemos que na função 'assertEqual' recebemos dois parâmetros, sendo que, será certo se os dois forem '=='


if __name__ == '__main__':
    unittest.main()
