from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from os.path import join


class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

    def inicializa_GUI(self):
        self.setWindowTitle("DCColgado")

        self.label_palabra_descrip = QLabel("PALABRA:")
        self.label_palabra = QLabel("")
        self.layout_palabra = QHBoxLayout()
        self.layout_palabra.addWidget(self.label_palabra_descrip)
        self.layout_palabra.addWidget(self.label_palabra)

        self.label_usadas_descrip = QLabel("LETRAS USADAS:")
        self.label_usadas = QLabel("-")
        self.layout_usadas = QHBoxLayout()
        self.layout_usadas.addWidget(self.label_usadas_descrip)
        self.layout_usadas.addWidget(self.label_usadas)

        self.label_disponibles_descrip = QLabel("LETRAS DISPONIBLES:")
        self.label_disponibles = QLabel("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
        self.layout_disponibles = QHBoxLayout()
        self.layout_disponibles.addWidget(self.label_disponibles_descrip)
        self.layout_disponibles.addWidget(self.label_disponibles)

        self.label_mensaje_descrip = QLabel("MENSAJE:")
        self.label_mensaje = QLabel("")
        self.layout_mensaje = QHBoxLayout()
        self.layout_mensaje.addWidget(self.label_mensaje_descrip)
        self.layout_mensaje.addWidget(self.label_mensaje)

        self.label_seleccionada_descrip = QLabel("LETRA SELECCIONADA:")
        self.label_seleccionada = QLabel("")
        self.layout_seleccionada = QHBoxLayout()
        self.layout_seleccionada.addWidget(self.label_seleccionada_descrip)
        self.layout_seleccionada.addWidget(self.label_seleccionada)


        self.boton_letra = QPushButton("Seleccionar letra")
        self.boton_letra.resize(self.boton_letra.sizeHint())
        self.boton_letra.clicked.connect(self.enviar_letra)

        self.boton_nuevo = QPushButton("Juego nuevo")
        self.boton_nuevo.resize(self.boton_nuevo.sizeHint())
        self.boton_nuevo.clicked.connect(self.reiniciar_senal)

        self.imagen = QLabel()
        self.imagen.setPixmap(QPixmap(join("images", "7.png")))

        self.layout_botones = QHBoxLayout()
        self.layout_botones.addStretch()
        self.layout_botones.addWidget(self.boton_letra)
        self.layout_botones.addWidget(self.boton_nuevo)
        self.layout_botones.addStretch()

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.imagen)
        self.layout_principal.addLayout(self.layout_palabra)
        self.layout_principal.addLayout(self.layout_usadas)
        self.layout_principal.addLayout(self.layout_disponibles)
        self.layout_principal.addLayout(self.layout_seleccionada)
        self.layout_principal.addLayout(self.layout_botones)
        self.layout_principal.addLayout(self.layout_mensaje)

        self.setLayout(self.layout_principal)

    def keyPressEvent(self, key_event):
        self.label_seleccionada.setText(key_event.text().upper())

    def enviar_letra(self):
        palabra = ""
        letra = self.label_seleccionada.text()
        dict_enviado = {"letra": letra, "palabra": palabra}
        self.enviar_letra_signal.emit(dict_enviado)

    def reiniciar_senal(self):
        self.reiniciar_signal.emit()
    
    def actualizar_ventana(self, data):
        if "gif" not in data:
            self.label_mensaje.setText(data["msg"])
            self.label_usadas.setText(data["usadas"])
            self.label_disponibles.setText(data["disponibles"])
            self.label_palabra.setText(data["palabra"])
            self.imagen.setPixmap(QPixmap(data["imagen"]))

        # iba a hacer el bonus pero no alcancé :(