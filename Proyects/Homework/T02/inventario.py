from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QGridLayout)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import (QPixmap, QFont)
import parametros_generales as pg
import parametros_plantas as plantas
from collections import defaultdict
from drag_drop import ItemDraggable


class VentanaInventario(QWidget):
    dict_items_signal = pyqtSignal(dict)
    datos_click_signal = pyqtSignal(list)

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.alto = 120
        self.label_inventario = QLabel("INVENTARIO:", self)
        self.label_inventario.setFont(QFont("Segoe", 18))
        self.layout_inventario = QHBoxLayout()
        self.layout_inventario.addStretch()
        self.layout_inventario.addWidget(self.label_inventario)
        self.inventario = QGridLayout()
        self.inventario.setAlignment(Qt.AlignLeft)
        self.layout_inventario.addStretch()
        self.layout_inventario.addLayout(self.inventario)
        self.layout_inventario.addStretch()
        self.setLayout(self.layout_inventario)
        self.posiciones_disp = [(i, j) for j in range(12) for i in range(3)]
        self.posiciones_disp.reverse()
        self.posiciones_ocupadas = defaultdict(list)
        self.dict_item = {}
        self.num_azadas = 0
        self.num_hachas = 0

    def agregar_item(self, valor):
        if valor == "choclo":
            cantidad = plantas.COSECHA_CHOCLOS
        elif valor == "alcachofa":
            cantidad = plantas.COSECHA_ALCACHOFAS
        else:
            cantidad = 1
        for i in range(cantidad):
            if self.posiciones_disp:
                posicion = self.posiciones_disp.pop()
                if valor in ["seed_c", "seed_a"]:
                    label_item = ItemDraggable(valor, posicion, self)
                else:
                    label_item = QLabel(valor, self)
                    pixmap_item = QPixmap(pg.PATH_TIENDA[valor]).scaled(QSize(pg.N, pg.N))
                    label_item.setPixmap(pixmap_item)
                self.dict_item[posicion] = label_item
                self.inventario.addWidget(label_item, *posicion)
                self.posiciones_ocupadas[valor].append(posicion)
                if valor == "hacha":
                    self.num_hachas += 1
                elif valor == "azada":
                    self.num_azadas += 1

# https://stackoverflow.com
# /questions/13184250/is-there-any-way-to-remove-a-qwidget-in-a-qgridlayout

    def eliminar_item(self, valor):
        if self.posiciones_ocupadas[valor]:
            posicion = self.posiciones_ocupadas[valor].pop()
            widget = self.dict_item[posicion]
            self.inventario.removeWidget(widget)
            widget.deleteLater()
            del widget
            self.posiciones_disp.append(posicion)
            if valor == "hacha":
                self.num_hachas -= 1
            elif valor == "azada":
                self.num_azadas -= 1

    def gastar_item(self, lista):
        valor = lista[0]
        posicion = lista[1]
        self.posiciones_ocupadas[valor].remove(posicion)
        widget = self.dict_item[posicion]
        self.inventario.removeWidget(widget)
        widget.deleteLater()
        del widget
        self.posiciones_disp.append(posicion)

    def enviar_items(self):
        datos_items = defaultdict(int)
        for valor in self.posiciones_ocupadas:
            datos_items[valor] = len(self.posiciones_ocupadas[valor])
        self.dict_items_signal.emit(datos_items)

    def enviar_datos_click(self, pos_click):
        datos = [pos_click, self.num_azadas, self.num_hachas]
        self.datos_click_signal.emit(datos)
