# Tirar Dados de la suerte
import random, time


class LanzarDado:
    def __init__(self, numero_dados, numero_caras):
        self.numero_dados = numero_dados
        self.numero_caras = numero_caras

    def lanzar(self):
        self.suerte = random.randint(1, self.numero_caras)

    def mostrar(self):
        if self.numero_dados > 1:
            for i in range(self.numero_dados):
                print(self.suerte)
        else:
            print(self.suerte)

        # print('Tirando dados...')
        # time.sleep(self.suerte)



numero = LanzarDado(3, 5)
numero.lanzar()
numero.mostrar()