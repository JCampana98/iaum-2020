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
    piso_aux = Piso()
    posicion = 0
    direccion = 'derecha'
    giros = 0
    movimientos = 0
    condicion_piso = []

    def set_direccion_ideal(self, mitad_piso):
        if self.posicion >= mitad_piso:
            self.direccion = 'derecha'
        if self.posicion < mitad_piso:
            self.direccion = 'izquierda'

    def set_condicion_piso(self, len_piso):
        for cond in range(0, len_piso):
            self.condicion_piso.append(0)

    def update_condicion_piso(self, condicion):
        if condicion == pared:
            self.condicion_piso[self.posicion] = -1
        if condicion == 'limpieza':
            self.condicion_piso[self.posicion] = self.condicion_piso[self.posicion] + 1
        if condicion == 'avance':
            self.condicion_piso[self.posicion] = self.condicion_piso[self.posicion] + 1

    def avanzar(self):
        self.movimientos += 1
        if self.condicion_piso[self.posicion] == 0:
            self.update_condicion_piso('avance')
            print('Por aca no habia pasado \n')
        elif self.condicion_piso[self.posicion] == -1:
            print('Me choque con una pared \n')
        elif self.condicion_piso[self.posicion] > 1:
            print('Aca limpie \n')
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance \n')

    def girar_izquierda(self):
        self.movimientos += 1
        self.giros += 1
        self.direccion = 'izquierda'
        self.posicion -= 1
        print('Gire a la izquierda \n')

    def girar_derecha(self):
        self.movimientos += 1
        self.giros += 1
        self.direccion = 'derecha'
        self.posicion += 1
        print('Gire a la derecha \n')

    def limpiar(self, estado):
        self.movimientos += 1
        if estado == poco:
            self.update_condicion_piso('limpieza')
            print('Limpie \n')
            return limpio
        elif estado == sucio:
            self.update_condicion_piso('limpieza')
            print('Limpie \n')
            return poco
        elif estado == permanente:
            self.update_condicion_piso('limpieza')
            print('Limpie \n')
            return permanente

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

    aspiradora = Aspiradora()
    aspiradora.posicion = random.randrange(1, len(piso.fila_baldosas) - 1)
    aspiradora.set_condicion_piso(len(piso.fila_baldosas))
    aspiradora.set_direccion_ideal(len(piso.fila_baldosas)/2)

    print('Estado inicial de la aspiradora y el piso')
    piso.mostrar_piso()
    aspiradora.mostrar_aspiradora(len(piso.fila_baldosas))

    # El programa se detiene cuando se toco dos paredes, es decir, se realizaron dos giros

    while aspiradora.giros < 2:
        pared_tocada = False
        if piso.fila_baldosas[aspiradora.posicion].estado == pared:
            aspiradora.update_condicion_piso(pared)
            pared_tocada = True
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
            elif aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
        if aspiradora.condicion_piso[aspiradora.posicion] < 1 and aspiradora.condicion_piso[aspiradora.posicion] != -1:
            for limpieza in range(0, 2):
                if piso.fila_baldosas[aspiradora.posicion].estado != limpio:
                    piso.fila_baldosas[aspiradora.posicion].estado = \
                        aspiradora.limpiar(piso.fila_baldosas[aspiradora.posicion].estado)
        if not pared_tocada:
            aspiradora.avanzar()
        piso.mostrar_piso()
        aspiradora.mostrar_aspiradora(len(piso.fila_baldosas))

    print('Se han realizado: ', aspiradora.movimientos, 'movimientos')
