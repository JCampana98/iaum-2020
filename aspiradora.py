import random

# Estado de las baldosas

limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
piso = [pared, limpio, sucio, poco, permanente, limpio, limpio, pared]


class Aspiradora:
    posicion = random.randrange(len(piso))
    direccion = 'derecha'
    movimientos = 0

    def avanzar(self):
        self.movimientos += 1
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance \n')

    def girar_izquierda(self):
        self.movimientos += 1
        self.direccion = 'izquierda'
        print('Gire a la izquierda \n')

    def girar_derecha(self):
        self.movimientos += 1
        self.direccion = 'derecha'
        print('Gire a la derecha \n')

    def limpiar(self):
        self.movimientos += 1
        print('Limpie \n')

    def revisar_suciedad(self):
        self.movimientos += 1
        print('Limpie \n')


if __name__ == '__main__':
    clean = False
    aspiradora = Aspiradora()
    for i in range(0, 100):
        if piso[aspiradora.posicion] == poco:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = poco
        elif piso[aspiradora.posicion] == permanente:
            aspiradora.limpiar()
        elif piso[aspiradora.posicion] == pared:
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
            if aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
        aspiradora.avanzar()
