from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout,
                             QVBoxLayout, QProgressBar)
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QFont
import parametros_generales as pg
from math import ceil


class VentanaStats(QWidget):
    cambio_dia_signal = pyqtSignal()
    salir_juego_signal = pyqtSignal()
    pausar_juego_signal = pyqtSignal()
    perder_partida_signal = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.ancho = 140
        self.label_stats = QLabel("STATS:", self)
        self.label_stats.setFont(QFont("Times", 18))
        self.label_stats.setAlignment(Qt.AlignCenter)
        self.label_dia = QLabel("Día: 0", self)
        self.label_dia.setFont(QFont("Times", 16))
        self.label_dia.setAlignment(Qt.AlignCenter)
        self.label_hora = QLabel("Hora: 00:00", self)
        self.label_hora.setFont(QFont("Times", 16))
        self.label_hora.setAlignment(Qt.AlignCenter)
        self.label_dinero = QLabel("$: " + str(pg.MONEDAS_INICIALES), self)
        self.label_dinero.setFont(QFont("Times", 16))
        self.label_dinero.setAlignment(Qt.AlignCenter)
        self.label_energia = QLabel("Energía:", self)
        self.label_energia.setFont(QFont("Times", 16))
        self.label_energia.setAlignment(Qt.AlignCenter)

        self.energia_disp = pg.ENERGIA_JUGADOR
        self.energia = QProgressBar(self)
        self.energia.setValue(ceil(self.energia_disp * 100 / pg.ENERGIA_JUGADOR))
        self.layout_energia = QHBoxLayout()
        self.layout_energia.addStretch()
        self.layout_energia.addWidget(self.energia)
        self.layout_energia.addStretch()

        self.boton_pausar = QPushButton("Pausar", self)
        self.boton_pausar.clicked.connect(self.pausar_juego)
        self.layout_pausar = QHBoxLayout()
        self.layout_pausar.addSpacing(14)
        self.layout_pausar.addWidget(self.boton_pausar)
        self.layout_pausar.addStretch()

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.clicked.connect(self.salir_juego)
        self.layout_salir = QHBoxLayout()
        self.layout_salir.addSpacing(14)
        self.layout_salir.addWidget(self.boton_salir)
        self.layout_salir.addStretch()

        self.layout_stats = QVBoxLayout()
        self.layout_stats.addSpacing(30)
        self.layout_stats.addWidget(self.label_stats)
        self.layout_stats.addWidget(self.label_dia)
        self.layout_stats.addWidget(self.label_hora)
        self.layout_stats.addWidget(self.label_dinero)
        self.layout_stats.addWidget(self.label_energia)
        self.layout_stats.addSpacing(-20)
        self.layout_stats.addLayout(self.layout_energia)
        self.layout_stats.addSpacing(100)
        self.layout_stats.addLayout(self.layout_pausar)
        self.layout_stats.addSpacing(0)
        self.layout_stats.addLayout(self.layout_salir)
        self.layout_stats.addSpacing(30)
        self.setLayout(self.layout_stats)

        self.reloj_interno = QTimer()
        self.reloj_interno.setInterval(pg.DURACION_MINUTO * 1000)
        self.reloj_interno.timeout.connect(self.actualizar_reloj)
        self.dia = 0
        self.hora = 0
        self.minuto = 0

    def iniciar_reloj(self):
        self.reloj_interno.start()

    def actualizar_reloj(self):
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
            if self.hora == 24:
                self.hora = 0
                self.dia += 1
                self.cambio_dia_signal.emit()
        str_dia = "Dia: " + str(self.dia)
        self.label_dia.setText(str_dia)
        str_hora = "{:02d}".format(self.hora)
        str_minuto = "{:02d}".format(self.minuto)
        self.label_hora.setText("Hora: " + str_hora + ":" + str_minuto)

    def dormir(self):
        self.minuto = 0
        self.hora = 0
        self.dia += 1
        str_dia = "Dia: " + str(self.dia)
        self.label_dia.setText(str_dia)
        str_hora = "{:02d}".format(self.hora)
        str_minuto = "{:02d}".format(self.minuto)
        self.label_hora.setText("Hora: " + str_hora + ":" + str_minuto)
        self.cambio_dia_signal.emit()

    def actualizar_dinero(self, dinero):
        self.label_dinero.setText("$: " + str(dinero))

    def salir_juego(self):
        self.salir_juego_signal.emit()

    def pausar_juego(self):
        self.reloj_interno.stop()
        self.pausar_juego_signal.emit()

    def trampa_dinero(self):
        dinero = self.label_dinero.text()
        dinero = int(dinero[3:])
        self.label_dinero.setText("$: " + str(dinero + pg.DINERO_TRAMPA))

    def actualizar_energia(self, gasto):
        self.energia_disp -= gasto
        if self.energia_disp <= 0:
            self.perder_partida_signal.emit()
        if self.energia_disp > pg.ENERGIA_JUGADOR:
            self.energia_disp = pg.ENERGIA_JUGADOR
        self.energia.setValue(ceil(self.energia_disp * 100 / pg.ENERGIA_JUGADOR))

    def trampa_energia(self):
        self.energia_disp = pg.ENERGIA_JUGADOR
        self.energia.setValue(ceil(self.energia_disp * 100 / pg.ENERGIA_JUGADOR))
