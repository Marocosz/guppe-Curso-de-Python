import unittest


from robo import Robo


class RoboTestes(unittest.TestCase):

    # Utilizando setUp não temos que criar em cada função teste um objeto da classe que estamos testando
    # fazemos apenas uma vez na função setUp()

    def setUp(self):
        print('setUp() está sendo executadon ')
        self.megaman = Robo('Mega Man', bateria=50)

    def teste_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def teste_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'Beep, beep, sou o Mega Man, o robo!')
        self.assertEqual(self.megaman.bateria, 49)

    def tearDown(self):
        print('TearDown() está sendo executado')
        # não é obrigatório de criar a função tearDown()


if __name__ == '__main__':
    unittest.main()