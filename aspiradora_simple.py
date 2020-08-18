import random

# Estado de las baldosas
limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'


class Baldosa:
    estado = limpio

    def set_estado(self):
        x = random.randrange(0, 3)

        if x == 0:
            self.estado = limpio

        if x == 1:
            self.estado = poco

        if x == 2:
            self.estado = sucio

        if x == 3:
            self.estado = permanente


class Piso:
    fila_baldosas = [Baldosa] * random.randrange(1, 10)

    def set_fila_baldosas(self):
        for j in range(0, len(self.fila_baldosas)):
            baldosa = Baldosa()
            baldosa.set_estado()

            self.fila_baldosas[j] = baldosa

    def set_paredes(self):
        baldosa = Baldosa()
        baldosa.estado = pared
        self.fila_baldosas.insert(0, baldosa)
        self.fila_baldosas.append(baldosa)

    def mostrar_piso(self):
        cadena = ''
        for j in range(0, len(self.fila_baldosas)):
            cadena = cadena + '|' + self.fila_baldosas[j].estado + '|'
        print(cadena)


class Aspiradora:
    posicion = 0
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

    def mostrar_aspiradora(self, len_piso):
        cadena = ''
        for cad in range(0, len_piso):
            if cad == self.posicion:
                cadena = cadena + '|A|'
            else:
                cadena = cadena + '| |'
        print(cadena)


if __name__ == '__main__':
    piso = Piso()
    piso.set_fila_baldosas()
    piso.set_paredes()
    piso.mostrar_piso()

    aspiradora = Aspiradora()
    aspiradora.posicion = random.randrange(1, len(piso.fila_baldosas) - 1)
    aspiradora.mostrar_aspiradora(len(piso.fila_baldosas))

    for i in range(0, 100):
        if piso.fila_baldosas[aspiradora.posicion].estado == pared:
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
                aspiradora.avanzar()
            elif aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
                aspiradora.avanzar()
        if piso.fila_baldosas[aspiradora.posicion].estado == poco:
            aspiradora.limpiar()
            piso.fila_baldosas[aspiradora.posicion].estado = limpio
        elif piso.fila_baldosas[aspiradora.posicion].estado == sucio:
            aspiradora.limpiar()
            piso.fila_baldosas[aspiradora.posicion].estado = poco
        elif piso.fila_baldosas[aspiradora.posicion].estado == permanente:
            aspiradora.limpiar()
        aspiradora.avanzar()

    print('Se han realizado: ', aspiradora.movimientos, 'movimientos')
