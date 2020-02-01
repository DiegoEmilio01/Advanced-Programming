from PyQt5.QtCore import QObject, pyqtSignal
import os
import parametros_generales as pg
from math import floor
from time import sleep


class ProcesadorInicio(QObject):

    respuesta_signal = pyqtSignal(bool)

    def procesar(self, texto):
        mapas = os.listdir("mapas")
        if texto in mapas:
            self.respuesta_signal.emit(True)
        else:
            self.respuesta_signal.emit(False)


class ProcesadorMapa(QObject):

    mapa_signal = pyqtSignal(list)

    def leer_mapa(self, texto):
        ruta_mapa = os.path.join("mapas", texto)
        with open(ruta_mapa, 'rt', encoding='utf-8') as file:
            mapa = [linea.strip().split(" ") for linea in file]
        self.mapa_signal.emit(mapa)

# código basado en la atudantía extra


class Personaje(QObject):

    refrescar_signal = pyqtSignal(dict)
    enviar_items_signal = pyqtSignal()
    dormir_signal = pyqtSignal()
    recoger_item_signal = pyqtSignal(tuple)
    recuperar_energia_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.y_min = 16
        self.x_min = 16
        self.ancho = 14
        self.alto = 30
        self.direccion = 'D'
        self._x = 16
        self._y = 16
        self.dinero = pg.MONEDAS_INICIALES

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if self.comprobar_posicion(self.y, value):
            self._x = value
            self.refrescar_signal.emit({
                "x": self.x,
                "y": self.y,
                "direccion": self.direccion
            })

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if self.comprobar_posicion(value, self.x):
            self._y = value
            self.refrescar_signal.emit({
                "x": self.x,
                "y": self.y,
                "direccion": self.direccion
            })

    def datos_mapa(self, datos):
        self.y_max = datos[0]
        self.x_max = datos[1]
        self.posiciones_piedras = datos[2]
        self.posiciones_tienda = datos[3]
        self.posiciones_casa = datos[4]
        self.posiciones_arboles = datos[5]
        self.posiciones_recolectables = datos[6]
        self.y = datos[7]
        self.x = datos[8]

    def comprobar_posicion(self, y, x):
        pos_1 = floor((y - 16) / pg.N)
        pos_2 = floor((y + self.alto - 15) / pg.N)
        pos_3 = floor((x - 16) / pg.N)
        pos_4 = floor((x + self.ancho - 15) / pg.N)
        set_pos = {(pos_1, pos_3), (pos_1, pos_4), (pos_2, pos_3), (pos_2, pos_4)}
        if (self.x_min > x) or (x + self.ancho > self.x_max):
            return False
        elif (self.y_min > y) or (y + self.alto > self.y_max):
            return False
        elif (set_pos & self.posiciones_piedras) or (set_pos & self.posiciones_arboles):
            return False
        elif set_pos & self.posiciones_tienda:
            self.enviar_items_signal.emit()
            return False
        elif set_pos & self.posiciones_casa:
            self.recuperar_energia_signal.emit(pg.ENERGIA_DORMIR)
            self.dormir_signal.emit()
            return False
        elif set_pos & self.posiciones_recolectables:
            lista_pos = list(set_pos & self.posiciones_recolectables)
            self.recoger_item_signal.emit(lista_pos[0])
            return True
        else:
            return True

    def moverse(self, event):
        if event == "R":
            self.direccion = "R"
            self.x += pg.VEL_MOVIMIENTO
        elif event == "L":
            self.direccion = "L"
            self.x -= pg.VEL_MOVIMIENTO
        elif event == "D":
            self.direccion = "D"
            self.y += pg.VEL_MOVIMIENTO
        elif event == "U":
            self.direccion = "U"
            self.y -= pg.VEL_MOVIMIENTO
