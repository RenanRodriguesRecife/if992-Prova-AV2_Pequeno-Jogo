from abc import ABC, abstractmethod

class Coisa(ABC):
    def __init__(self):
        self.simbolo = '-'
        self.visivel = True
        self.area = -1
        self.posicao = [0,0]

    @abstractmethod
    def reagirMovimento(self):
        pass

    @abstractmethod
    def entrarArea(self):
        pass

    @abstractmethod
    def sairArea(self):
        pass

    @abstractmethod
    def mover(self,direcao):
        pass