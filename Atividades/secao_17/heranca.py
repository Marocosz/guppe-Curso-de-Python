class Equipamento:

    def __init__(self, tipo, qualidade):
        self.__tipo = tipo
        self.__qualidade = qualidade

    def exibir(self):
        print(f'\nTipo: {self.__tipo}\n'
              f'Qualidade: {self.__qualidade}\n')

    @property
    def tipo(self):
        return self.__tipo

    @property
    def qualidade(self):
        return self.__qualidade

    @tipo.setter
    def settTipo(self, novo_tipo):
        self.__tipo = novo_tipo
        print('Você alterou o Tipo')

    @qualidade.setter
    def settQualidade(self, nova_qualidade):
        self.__qualidade = nova_qualidade
        print('Voce alterou a Qualidade')


class Computador(Equipamento):

    def __init__(self, tipo, qualidade, processador, ram):
        super().__init__(tipo, qualidade)
        self.__processador = processador
        self.__ram = ram

    def exibir(self):
        print(f'\nTipo: {self._Equipamento__tipo}\n'
              f'Qualidade: {self._Equipamento__qualidade}\n'
              f'Processador: {self.__processador}\n'
              f'Ram: {self.__ram}\n')

    @property
    def processador(self):
        return self.__processador

    @property
    def ram(self):
        return self.__ram

    @processador.setter
    def settProcessador(self, novo_processador):
        self.__processador = novo_processador
        print('Voce alterou o Processador')

    @ram.setter
    def settRam(self, nova_ram):
        self.__ram = nova_ram
        print('Voce alterou a Ram')


class TestaEquipamento:

    def main(self, nome1, nome2, tipo, qualidade, processador, ram):

        nome1 = Equipamento(tipo, qualidade)
        nome2 = Computador(tipo, qualidade, processador, ram)

        nome1.exibir()
        nome2.exibir()


teste1 = TestaEquipamento()

teste1.main('a1', 'b2', 'Comp', 'Boa', 'i5', 8)

comp1 = Computador('Notebook', 'bom', 'i5', 8)
comp1.processador
comp1.exibir()