from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import (QPixmap, QImage, QPalette, QFont, QBrush, QIcon)
import parametros_generales as pg
import parametros_precios as pp
from inventario import VentanaInventario
from mapa import VentanaMapa
from stats import VentanaStats
from math import floor


class VentanaInicio(QWidget):

    enviar_texto_signal = pyqtSignal(str)
    iniciar_mapa_signal = pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):

        self.setGeometry(500, 150, 400, 300)
        self.setWindowTitle("Menú de Inicio")
        self.setWindowIcon(QIcon(pg.PATH_LOGO))

        self.label_instruccion = QLabel("Ingrese el nombre del mapa a cargar:", self)
        self.label_instruccion.setAlignment(Qt.AlignCenter)

        self.label_mensaje = QLabel("", self)
        self.label_mensaje.setAlignment(Qt.AlignCenter)

        self.imagen = QLabel(self)
        self.imagen.setPixmap(QPixmap(pg.PATH_LOGO))
        self.layout_imagen = QHBoxLayout()
        self.layout_imagen.addStretch()
        self.layout_imagen.addWidget(self.imagen)
        self.layout_imagen.addStretch()

        self.label_editar = QLineEdit("", self)
        self.layout_editar = QHBoxLayout()
        self.layout_editar.addStretch()
        self.layout_editar.addWidget(self.label_editar)
        self.layout_editar.addStretch()

        self.boton_jugar = QPushButton("Jugar", self)
        self.boton_jugar.clicked.connect(self.enviar_texto)
        self.layout_boton = QHBoxLayout()
        self.layout_boton.addStretch()
        self.layout_boton.addWidget(self.boton_jugar)
        self.layout_boton.addStretch()

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addStretch()
        self.layout_principal.addLayout(self.layout_imagen)
        self.layout_principal.addSpacing(20)
        self.layout_principal.addWidget(self.label_instruccion)
        self.layout_principal.addSpacing(8)
        self.layout_principal.addLayout(self.layout_editar)
        self.layout_principal.addSpacing(8)
        self.layout_principal.addLayout(self.layout_boton)
        self.layout_principal.addSpacing(8)
        self.layout_principal.addWidget(self.label_mensaje)
        self.layout_principal.addStretch()
        self.setLayout(self.layout_principal)

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Return:
            self.enviar_texto_signal.emit(self.label_editar.text())

    def enviar_texto(self):
        self.enviar_texto_signal.emit(self.label_editar.text())

    def actualizar_ventana(self, respuesta):
        if respuesta:
            self.label_mensaje.setText("")
            self.hide()
            self.iniciar_mapa_signal.emit(self.label_editar.text())
        else:
            self.label_mensaje.setText("El texto ingresado es inválido.")


class VentanaPausa(QWidget):

    despausar_juego_signal = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.setWindowTitle('Menú de Pausa')
        self.setGeometry(500, 350, 260, 70)
        self.setWindowIcon(QIcon(pg.PATH_LOGO))
        self.label_pausa = QLabel("JUEGO PAUSADO", self)
        self.label_pausa.setFont(QFont("Times", 14))
        self.label_pausa.setAlignment(Qt.AlignCenter)

        self.boton_continuar = QPushButton("Continuar", self)
        self.boton_continuar.clicked.connect(self.despausar_juego)

        self.layout_continuar = QHBoxLayout()
        self.layout_continuar.addStretch()
        self.layout_continuar.addWidget(self.boton_continuar)
        self.layout_continuar.addStretch()

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.label_pausa)
        self.layout_principal.addLayout(self.layout_continuar)
        self.setLayout(self.layout_principal)
        fondo = QImage(pg.PATH_FONDO_MAPA)
        fondo_scaled = fondo.scaled(QSize(262, 75))
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo_scaled))
        self.setPalette(palette)

    def pausar_juego(self):
        self.show()

    def despausar_juego(self):
        self.hide()
        self.despausar_juego_signal.emit()


class VentanaJuego(QWidget):

    moverse_signal = pyqtSignal(str)
    enviar_datos_signal = pyqtSignal(list)
    trampa_dinero_signal = pyqtSignal()
    trampa_energia_signal = pyqtSignal()
    enviar_click_signal = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menú de Juego')
        self.setWindowIcon(QIcon(pg.PATH_LOGO))
        self.mapa = VentanaMapa(self)
        self.inventario = VentanaInventario(self)
        self.stats = VentanaStats(self)

    def iniciar_juego(self):
        tamano = (self.mapa.ancho_pixeles, self.mapa.alto_pixeles)
        separador_1 = 36
        separador_2 = 50
        self.setGeometry(270, 80, tamano[0] + self.stats.ancho + separador_1,
                         tamano[1] + self.inventario.alto + separador_1)
        self.mapa.move(5, 5)
        self.inventario.setGeometry(5, self.mapa.alto_pixeles + separador_1,
                                    self.mapa.ancho_pixeles,
                                    self.inventario.alto)
        self.stats.setGeometry(self.mapa.ancho_pixeles + separador_2, 5,
                               self.stats.ancho, self.mapa.alto_pixeles +
                               self.inventario.alto + separador_1)
        fondo = QImage(pg.PATH_FONDO_MAPA)
        fondo_scaled = fondo.scaled(QSize(tamano[0] + 32, tamano[1] + 12))
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo_scaled))
        self.setPalette(palette)

        self.personaje_front = QLabel(self)
        self.skin = QPixmap(pg.PATHS_MOV[("D", 1)])
        self.personaje_front.setPixmap(self.skin)
        self.personaje_front.move(self.mapa.pos_inicial[1] * pg.N + 16,
                                  self.mapa.pos_inicial[0] * pg.N + 16)
        self._estado_skin = 1

        self.trampa_dinero = set()
        self.trampa_energia = set()

        self.enviar_datos_signal.emit([
            15 + self.mapa.alto_pixeles,
            15 + self.mapa.ancho_pixeles,
            self.mapa.pos_piedras,
            self.mapa.pos_tienda,
            self.mapa.pos_casa,
            self.mapa.pos_arboles,
            self.mapa.pos_recolectables,
            self.mapa.pos_inicial[0] * pg.N + 16,
            self.mapa.pos_inicial[1] * pg.N + 16
        ])
        self.show()

    @property
    def estado_skin(self):
        return self._estado_skin

    @estado_skin.setter
    def estado_skin(self, value):
        self._estado_skin = value if value < 4 else 1

    def mousePressEvent(self, event):
        pos_click = (floor((event.y() - 16) / pg.N), floor((event.x() - 16) / pg.N))
        self.enviar_click_signal.emit(pos_click)

    def keyPressEvent(self, event):
        dict_movimiento = {
            Qt.Key_D: 'R',
            Qt.Key_A: 'L',
            Qt.Key_W: 'U',
            Qt.Key_S: 'D'
        }
        if event.key() in dict_movimiento:
            self.moverse_signal.emit(dict_movimiento[event.key()])

        list_trampa_dinero = [Qt.Key_M , Qt.Key_N, Qt.Key_Y]
        if event.key() in list_trampa_dinero:
            self.trampa_dinero.add(event.key())
            if len(list(self.trampa_dinero)) == 3:
                self.trampa_dinero = set()
                self.trampa_dinero_signal.emit()

        list_trampa_energia = [Qt.Key_K , Qt.Key_I, Qt.Key_P]
        if event.key() in list_trampa_energia:
            self.trampa_energia.add(event.key())
            if len(list(self.trampa_energia)) == 3:
                self.trampa_energia = set()
                self.trampa_energia_signal.emit()

    def keyReleaseEvent(self, event):
        list_trampa_dinero = [Qt.Key_M , Qt.Key_N, Qt.Key_Y]
        if event.key() in list_trampa_dinero:
            self.trampa_dinero.discard(event.key())

        list_trampa_energia = [Qt.Key_K , Qt.Key_I, Qt.Key_P]
        if event.key() in list_trampa_energia:
            self.trampa_energia.discard(event.key())

    def refrescar_pantalla(self, movimiento):
        direccion = movimiento["direccion"]
        self.estado_skin += 1
        self.skin = QPixmap(pg.PATHS_MOV[(direccion, self.estado_skin)])
        self.personaje_front.setPixmap(self.skin)
        self.personaje_front.move(movimiento["x"], movimiento["y"])

    def ocultar_juego(self):
        self.hide()

    def mostrar_juego(self):
        self.show()

    def terminar_juego(self):
        self.close()


class VentanaFinal(QWidget):

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.setWindowTitle('Partida Terminada')
        self.setGeometry(500, 350, 260, 70)
        self.setWindowIcon(QIcon(pg.PATH_LOGO))

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.clicked.connect(self.terminar_juego)

        self.layout_salir = QHBoxLayout()
        self.layout_salir.addStretch()
        self.layout_salir.addWidget(self.boton_salir)
        self.layout_salir.addStretch()

        fondo = QImage(pg.PATH_FONDO_MAPA)
        fondo_scaled = fondo.scaled(QSize(262, 75))
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo_scaled))
        self.setPalette(palette)

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

    def perder_juego(self):
        self.label_estado = QLabel("¡JUEGO PERDIDO!", self)
        self.label_estado.setFont(QFont("Times", 14))
        self.label_estado.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.label_estado)
        self.layout_principal.addLayout(self.layout_salir)
        self.show()

    def ganar_juego(self):
        self.label_estado = QLabel("¡JUEGO GANADO!", self)
        self.label_estado.setFont(QFont("Times", 14))
        self.label_estado.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.label_estado)
        self.layout_principal.addLayout(self.layout_salir)
        self.show()

    def terminar_juego(self):
        self.close()
