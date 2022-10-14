class TecladoListener(self):
    def __init__(self):
        self.tecla = ''

    def getEntradaTeclado(self):
        self.tecla = input()[0]

    def consumirEvento(self):
        saida = self.tecla
        self.tecla = ''
        return saida