from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import QPixmap
import parametros_generales as pg
import parametros_acciones as pa
from collections import defaultdict
from random import random, sample
from drag_drop import LugarDrop, ItemDespawneable


class VentanaMapa(QWidget):

    enviar_mapa_signal = pyqtSignal(str)
    iniciar_juego_signal = pyqtSignal()
    enviar_item_signal = pyqtSignal(list)
    item_recolectado_signal = pyqtSignal(str)
    gastar_energia_signal = pyqtSignal(int)

    def __init__(self, *args):
        super().__init__(*args)

    def iniciar_mapa(self, mapa_elegido):
        self.enviar_mapa_signal.emit(mapa_elegido)

    def construir_mapa(self, lista_mapa):
        self.ancho = len(lista_mapa[0])
        self.ancho_pixeles = (self.ancho) * pg.N
        self.alto = len(lista_mapa)
        self.alto_pixeles = (self.alto) * pg.N
        self.pos_piedras = set()
        self.pos_tienda = set()
        self.pos_casa = set()
        self.pos_pastos = set()
        self.pos_arboles = set()
        self.dict_arboles = {}
        self.pos_recolectables = set()
        self.dict_recolectables = {}
        self.mapa = QGridLayout()
        self.mapa.setSpacing(0)
        self.arado = []
        self.despawneables = []
        posiciones = [(i, j) for i in range(self.alto) for j in range(self.ancho)]
        intento = defaultdict(int)
        for y, x in posiciones:
            valor = lista_mapa[y][x]
            if valor == "R":
                self.agregar_mapita("O", y, x, 1)
                self.agregar_mapita(valor, y, x, 1)
                self.pos_piedras.add((y, x))
            elif valor in ["T", "H"]:
                self.agregar_mapita("O", y, x, 1)
                intento[valor] += 1
                if intento[valor] == 4:
                    if valor == "H":
                        self.pos_inicial = (y + 1, x - 1)
                    self.agregar_mapita(valor, y-1, x-1, 2)
                if valor == "H":
                    self.pos_casa.add((y, x))
                else:
                    self.pos_tienda.add((y, x))
            elif valor == "C":
                self.agregar_mapita(valor, y, x, 1)
                fondo_mapa = QPixmap(pg.PATH_MAPA[valor])
                mapita_scaled = fondo_mapa.scaled(QSize(pg.N, pg.N))
                mapita = LugarDrop("D", y, x, self)
                mapita.setPixmap(mapita_scaled)
                self.arado.append(mapita)
                self.mapa.addWidget(mapita, y, x)
            else:
                self.agregar_mapita(valor, y, x, 1)
                self.pos_pastos.add((y, x))
        self.setLayout(self.mapa)
        for mapita in self.arado:
            mapita.gasto_item_signal.connect(self.item_gastado)
        self.iniciar_juego_signal.emit()

    def agregar_mapita(self, valor, y, x, escala):
        fondo_mapa = QPixmap(pg.PATH_MAPA[valor])
        mapita_scaled = fondo_mapa.scaled(QSize(pg.N * escala, pg.N * escala))
        mapita = QLabel(valor, self)
        mapita.posicion = (y, x)
        mapita.setPixmap(mapita_scaled)
        self.mapa.addWidget(mapita, y, x, escala, escala)

    def item_gastado(self, lista):
        self.enviar_item_signal.emit(lista)

    def pausar(self):
        for planta in self.arado:
            if planta.plantado:
                planta.reloj_interno.stop()
        for item in self.despawneables:
            item.reloj_interno.stop()

    def despausar(self):
        for planta in self.arado:
            if planta.plantado:
                planta.reloj_interno.start()
        for item in self.despawneables:
            item.reloj_interno.start()

    def cambio_dia(self):
        probabilidad_arbol = random()
        probabilidad_oro = random()
        if (probabilidad_arbol <= pg.PROB_ARBOL) and (len(self.pos_pastos) > 0):
            pos = sample(self.pos_pastos, 1)[0]
            self.pos_pastos.discard(pos)
            pixmap_arbol = QPixmap(pg.PATH_MAPA["A"]).scaled(QSize(pg.N, pg.N))
            arbol = QLabel("A", self)
            arbol.posicion = pos
            arbol.setPixmap(pixmap_arbol)
            self.mapa.addWidget(arbol, *pos)
            self.pos_arboles.add(pos)
            self.dict_arboles[pos] = arbol
        elif (probabilidad_oro <= pg.PROB_ORO) and (len(self.pos_pastos) > 0):
            pos = sample(self.pos_pastos, 1)[0]
            self.pos_pastos.discard(pos)
            pixmap_oro = QPixmap(pg.PATH_MAPA["oro"]).scaled(QSize(pg.N, pg.N))
            oro = ItemDespawneable("oro", pos, self)
            oro.despawn_signal.connect(self.despawnear_item)
            oro.setPixmap(pixmap_oro)
            self.despawneables.append(oro)
            self.mapa.addWidget(oro, *pos)
            self.pos_recolectables.add(pos)
            self.dict_recolectables[pos] = oro

    def recibir_click(self, datos):
        posicion_click = datos[0]
        azada = True if datos[1] > 0 else False
        hacha = True if datos[2] > 0 else False
        if (posicion_click in self.pos_arboles) and hacha:
            widget = self.dict_arboles[posicion_click]
            self.mapa.removeWidget(widget)
            widget.deleteLater()
            del widget
            self.pos_arboles.discard(posicion_click)
            pixmap_rama = QPixmap(pg.PATH_MAPA["rama"]).scaled(QSize(pg.N, pg.N))
            rama = ItemDespawneable("rama", posicion_click, self)
            rama.despawn_signal.connect(self.despawnear_item)
            rama.setPixmap(pixmap_rama)
            self.despawneables.append(rama)
            self.mapa.addWidget(rama, *posicion_click)
            self.pos_recolectables.add(posicion_click)
            self.dict_recolectables[posicion_click] = rama
            self.gastar_energia_signal.emit(pa.ENERGIA_HERRAMIENTA)
        elif (posicion_click in self.pos_pastos) and azada:
            self.agregar_mapita("C", *posicion_click, 1)
            pixmap_arado = QPixmap(pg.PATH_MAPA["C"]).scaled(QSize(pg.N, pg.N))
            mapita = LugarDrop("D", *posicion_click, self)
            mapita.setPixmap(pixmap_arado)
            self.arado.append(mapita)
            self.pos_pastos.discard(posicion_click)
            self.mapa.addWidget(mapita, *posicion_click)
            self.gastar_energia_signal.emit(pa.ENERGIA_HERRAMIENTA)
        for arado in self.arado:
            if (arado.posicion == posicion_click) and (arado.stage_actual == arado.stage_max):
                arado.cosechar()
                valor_2 = "choclo" if arado.valor == "seed_c" else "alcachofa"
                pixmap_arado = QPixmap(pg.PATH_MAPA[valor_2]).scaled(QSize(pg.N, pg.N))
                fruto = QLabel(valor_2, self)
                fruto.valor = valor_2
                fruto.setPixmap(pixmap_arado)
                self.mapa.addWidget(fruto, *posicion_click)
                self.pos_recolectables.add(posicion_click)
                self.dict_recolectables[posicion_click] = fruto
                self.gastar_energia_signal.emit(pa.ENERGIA_COSECHAR)

    def despawnear_item(self, pos):
        self.pos_recolectables.remove(pos)
        widget = self.dict_recolectables[pos]
        self.despawneables.remove(widget)
        self.mapa.removeWidget(widget)
        widget.deleteLater()
        del widget
        self.pos_pastos.add(pos)

    def recolectar_item(self, pos):
        self.pos_recolectables.remove(pos)
        widget = self.dict_recolectables[pos]
        if widget in self.despawneables:
            self.despawneables.remove(widget)
        if widget.valor not in ["choclo", "alcachofa"]:
            self.pos_pastos.add(pos)
        self.item_recolectado_signal.emit(widget.valor)
        self.mapa.removeWidget(widget)
        widget.deleteLater()
        del widget
        self.gastar_energia_signal.emit(pa.ENERGIA_RECOGER)
