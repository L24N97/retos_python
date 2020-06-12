# Tirar Dados de la suerte
import random


class Dados:
    def __init__(self, numero_dados, numero_caras):
        self.numero_dados = numero_dados
        self.numero_caras = numero_caras

    def aleatorio(self):
        if self.numero_dados > 0 and self.numero_caras > 1:
            for cara in range(self.numero_caras):
                self.suerte = random.randint(1, self.numero_caras)

    def __repr__(self):
        pass

