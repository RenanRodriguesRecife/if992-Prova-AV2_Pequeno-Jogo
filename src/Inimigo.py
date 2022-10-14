from abc import ABC, abstractmethod
import random

class Inimigo(Coisa,ABC):
    def __init__(self):
        self.simbolo = 'i'
        
    def escolherAcao(self):
        return random.choice(["cima","baixo","esquerda","direita"])


    