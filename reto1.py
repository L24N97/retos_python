# Tirar Dados de la suerte
import random, time


class LanzarDado:
    def __init__(self, numero_dados, numero_caras):
        self.numero_dados = numero_dados
        self.numero_caras = numero_caras

    def mostrar(self):
        self.resultado = []

        if self.numero_dados >= 1:
            for i in range(0,self.numero_dados):
                self.resultado.append(random.randint(1, self.numero_caras))
                self.array = [str(a) for a in self.resultado]
        print('Tirando dados...')
        time.sleep( self.numero_caras )

        print( '\n'.join(self.array) )
        print('Tu resultado es: {}'.format( sum(self.resultado) ) )

def main():

    num_dados = int(input( '¿Cuantos dados deseas? ~> '))
    num_caras = int(input( '¿Cuantas caras deseas? ~> '))

    while True:
        lanzamiento = LanzarDado(num_dados, num_caras)
        lanzamiento.mostrar()
        continuar = input('¿Desea continuar? y|n ')

        if continuar == 'y':
            num_dados = int(input('¿Cuantos dados deseas? ~> '))
            num_caras = int(input('¿Cuantas caras deseas? ~> '))
        if continuar == 'n':
            break

if __name__ == '__main__':
    main()


