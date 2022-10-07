from abc import ABC, abstractmethod

class Inimigo(Coisa,ABC):
    def __init__(self):
        self.simbolo = 'i'
        
    def escolherAcao(self):
        pass