from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import (QPixmap, QImage, QPalette, QFont, QBrush, QIcon)
import parametros_generales as pg
import parametros_precios as pp


class VentanaTienda(QWidget):

    enviar_compra_signal = pyqtSignal(str)
    venta_item_signal = pyqtSignal(str)
    ocultar_tienda_signal = pyqtSignal(int)
    mostrar_juego_signal = pyqtSignal()
    ganar_partida_signal = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.dinero = pg.MONEDAS_INICIALES
        self.setWindowTitle('Menú de la Tienda')
        self.move(300, 200)
        self.setWindowIcon(QIcon(pg.PATH_LOGO))
        self.grid_tools = QGridLayout()
        self.grid_recursos = QGridLayout()
        self.label_item = QLabel("ITEM", self)
        self.label_item.setFont(QFont("Times", 16))
        self.label_item_2 = QLabel("ITEM", self)
        self.label_item_2.setFont(QFont("Times", 16))
        self.label_precio = QLabel("PRECIO", self)
        self.label_precio.setFont(QFont("Times", 16))
        self.label_precio_2 = QLabel("PRECIO", self)
        self.label_precio_2.setFont(QFont("Times", 16))
        self.label_accion_0 = QLabel("ACCIONES", self)
        self.label_accion_0.setFont(QFont("Times", 16))
        self.label_accion_1 = QLabel("POSIBLES", self)
        self.label_accion_1.setFont(QFont("Times", 16))
        self.label_accion_2 = QLabel("ACCION", self)
        self.label_accion_2.setFont(QFont("Times", 16))
        self.label_dinero = QLabel("Dinero:", self)
        self.label_dinero.setFont(QFont("Times", 16))
        self.label_dinero.setAlignment(Qt.AlignCenter)
        self.label_dinero_2 = QLabel("$" + str(self.dinero), self)
        self.label_dinero_2.setFont(QFont("Times", 14))
        self.label_dinero_2.setAlignment(Qt.AlignCenter)

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.clicked.connect(self.ocultar_tienda)
        self.boton_salir.clicked.connect(self.mostrar_juego)

        self.layout_derecho = QGridLayout()
        self.layout_derecho.setAlignment(Qt.AlignTop)
        self.layout_derecho.addWidget(self.label_dinero, 0, 0)
        self.layout_derecho.addWidget(self.label_dinero_2, 1, 0)
        self.layout_derecho.addWidget(self.boton_salir, 2, 0)

        self.grid_tools.addWidget(self.label_item, 0, 0)
        self.grid_tools.addWidget(self.label_precio, 0, 1)
        self.grid_tools.addWidget(self.label_accion_0, 0, 2)
        self.grid_tools.addWidget(self.label_accion_1, 0, 3)
        self.grid_recursos.addWidget(self.label_item_2, 0, 0)
        self.grid_recursos.addWidget(self.label_precio_2, 0, 1)
        self.grid_recursos.addWidget(self.label_accion_2, 0, 2)

        self.dict_botones_compra = {}
        self.dict_botones_venta = {}

        self.agregar_a_grilla(0, "azada", "$" + str(pp.PRECIO_AZADA), 1)
        self.agregar_a_grilla(0, "hacha", "$" + str(pp.PRECIO_HACHA), 2)
        self.agregar_a_grilla(0, "seed_c", "$" + str(pp.PRECIO_SEMILLA_CHOCLOS), 3)
        self.agregar_a_grilla(0, "seed_a", "$" + str(pp.PRECIO_SEMILLA_ALCACHOFAS), 4)
        self.agregar_a_grilla(1, "alcachofa", "$" + str(pp.PRECIO_ALACACHOFAS), 1)
        self.agregar_a_grilla(1, "choclo", "$" + str(pp.PRECIO_CHOCLOS), 2)
        self.agregar_a_grilla(1, "rama", "$" + str(pp.PRECIO_LEÑA), 3)
        self.agregar_a_grilla(1, "oro", "$" + str(pp.PRECIO_ORO), 4)
        self.agregar_a_grilla(1, "ticket", "$" + str(pp.PRECIO_TICKET), 5)

        self.grid_recursos.setAlignment(Qt.AlignTop)
        self.grid_tools.setAlignment(Qt.AlignTop)
        self.layout_principal = QHBoxLayout()
        self.layout_principal.addSpacing(15)
        self.layout_principal.addLayout(self.grid_tools)
        self.layout_principal.addSpacing(30)
        self.layout_principal.addLayout(self.grid_recursos)
        self.layout_principal.addSpacing(30)
        self.layout_principal.addLayout(self.layout_derecho)
        self.layout_principal.addSpacing(15)
        self.layout_principal_2 = QVBoxLayout()
        self.layout_principal_2.addSpacing(15)
        self.layout_principal_2.addLayout(self.layout_principal)
        self.layout_principal_2.addSpacing(15)
        self.setLayout(self.layout_principal_2)
        fondo = QImage(pg.PATH_FONDO_MAPA)
        fondo_scaled = fondo.scaled(QSize(770, 350))
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo_scaled))
        self.setPalette(palette)

    def agregar_a_grilla(self, grilla, valor, precio, fila):
        label_2 = QLabel(precio, self)
        label_2.setFont(QFont("Times", 14))
        label_2.setAlignment(Qt.AlignCenter)
        item = QPixmap(pg.PATH_TIENDA[valor]).scaled(QSize(pg.N * 1.5, pg.N * 1.5))
        label_1 = QLabel(valor, self)
        label_1.setPixmap(item)
        text_boton = "Comprar" if valor == "ticket" else "Vender"
        boton_1 = QPushButton(text_boton, self)
        if not grilla:
            boton_2 = QPushButton("Comprar", self)
            boton_2.clicked.connect(self.comprar_item)
            boton_1.clicked.connect(self.vender_tool)
            self.grid_tools.addWidget(label_1, fila, 0)
            self.grid_tools.addWidget(label_2, fila, 1)
            self.grid_tools.addWidget(boton_1, fila, 2)
            self.grid_tools.addWidget(boton_2, fila, 3)
            self.dict_botones_compra[valor] = boton_2
            self.dict_botones_venta[valor] = boton_1

        else:
            if valor == "ticket":
                boton_1.clicked.connect(self.ganar_partida)
                self.dict_botones_compra[valor] = boton_1

            else:
                boton_1.clicked.connect(self.vender_recurso)
                self.dict_botones_venta[valor] = boton_1
            self.grid_recursos.addWidget(label_1, fila, 0)
            self.grid_recursos.addWidget(label_2, fila, 1)
            self.grid_recursos.addWidget(boton_1, fila, 2)

    def mostrar_tienda(self, datos):
        self.dict_items = datos
        cantidad_items = 0
        for valor in datos:
            cantidad_items += datos[valor]
        self.cantidad_items = cantidad_items
        self.actualizar_botones_compra()
        self.actualizar_botones_venta()
        self.show()

    def ocultar_tienda(self):
        self.hide()

    def mostrar_juego(self):
        self.ocultar_tienda_signal.emit(self.dinero)
        self.mostrar_juego_signal.emit()

    def comprar_item(self):
        id_boton = self.grid_tools.indexOf(self.sender())
        posicion_boton = self.grid_tools.getItemPosition(id_boton)
        valores = {1: "azada", 2: "hacha", 3: "seed_c", 4: "seed_a"}
        valor = valores[posicion_boton[0]]
        self.dinero -= self.calcular_costo(valor)
        self.dict_items[valor] += 1
        self.cantidad_items += 1
        self.label_dinero_2.setText("$" + str(self.dinero))
        self.actualizar_botones_compra()
        self.actualizar_botones_venta()
        self.enviar_compra_signal.emit(valor)

    def vender_tool(self):
        boton = self.sender()
        id_boton = self.grid_tools.indexOf(self.sender())
        posicion_boton = self.grid_tools.getItemPosition(id_boton)
        valores = {1: "azada", 2: "hacha", 3: "seed_c", 4: "seed_a"}
        valor = valores[posicion_boton[0]]
        self.dinero += self.calcular_costo(valor)
        self.dict_items[valor] -= 1
        self.cantidad_items -= 1
        self.label_dinero_2.setText("$" + str(self.dinero))
        self.actualizar_botones_compra()
        self.actualizar_botones_venta()
        self.venta_item_signal.emit(valor)

    def vender_recurso(self):
        boton = self.sender()
        id_boton = self.grid_recursos.indexOf(self.sender())
        posicion_boton = self.grid_recursos.getItemPosition(id_boton)
        valores = {1: "alcachofa", 2: "choclo", 3: "rama", 4: "oro"}
        valor = valores[posicion_boton[0]]
        self.dinero += self.calcular_costo(valor)
        self.dict_items[valor] -= 1
        self.cantidad_items -= 1
        self.label_dinero_2.setText("$" + str(self.dinero))
        self.actualizar_botones_compra()
        self.actualizar_botones_venta()
        self.venta_item_signal.emit(valor)

    def actualizar_botones_compra(self):
        for valor in ["azada", "hacha", "seed_c", "seed_a", "ticket"]:
            if self.dinero < self.calcular_costo(valor) or self.cantidad_items == pg.MAX_ITEMS:
                self.dict_botones_compra[valor].setEnabled(False)
            else:
                self.dict_botones_compra[valor].setEnabled(True)

    def actualizar_botones_venta(self):
        for valor in ["azada", "hacha", "seed_c", "seed_a", "alcachofa", "choclo", "rama", "oro"]:
            if self.dict_items[valor] == 0:
                self.dict_botones_venta[valor].setEnabled(False)
            else:
                self.dict_botones_venta[valor].setEnabled(True)

    def calcular_costo(self, valor):
        if valor == "azada":
            return pp.PRECIO_AZADA
        if valor == "hacha":
            return pp.PRECIO_HACHA
        if valor == "seed_c":
            return pp.PRECIO_SEMILLA_CHOCLOS
        if valor == "seed_a":
            return pp.PRECIO_SEMILLA_ALCACHOFAS
        if valor == "alcachofa":
            return pp.PRECIO_ALACACHOFAS
        if valor == "choclo":
            return pp.PRECIO_CHOCLOS
        if valor == "rama":
            return pp.PRECIO_LEÑA
        if valor == "oro":
            return pp.PRECIO_ORO
        if valor == "ticket":
            return pp.PRECIO_TICKET

    def trampa_dinero(self):
        self.dinero += pg.DINERO_TRAMPA
        self.label_dinero_2.setText("$" + str(self.dinero))

    def ganar_partida(self):
        self.ganar_partida_signal.emit()
