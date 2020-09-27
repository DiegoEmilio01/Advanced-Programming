from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import (QPixmap, QImage, QPalette, QFont, QBrush, QIcon)
from os import path


class VentanaInicio(QWidget):

    usuario_interfaz_procesador = pyqtSignal(str)
    mostrar_principal_signal = pyqtSignal(dict)

    def __init__(self, path_logo, *args):
        super().__init__(*args)

        self.setGeometry(500, 150, 400, 300)
        self.setWindowTitle("Menú de Inicio")

        path_logo = path.join(*path_logo)
        self.setWindowIcon(QIcon(path_logo))

        self.imagen = QLabel(self)
        self.imagen.setPixmap(QPixmap(path_logo).scaled(QSize(360, 120)))
        self.layout_imagen = QHBoxLayout()
        self.layout_imagen.addStretch()
        self.layout_imagen.addWidget(self.imagen)
        self.layout_imagen.addStretch()

        self.label_instruccion = QLabel("Ingrese el nombre del USUARIO a cargar:", self)
        self.label_instruccion.setFont(QFont("Times", 16))
        self.label_instruccion.setAlignment(Qt.AlignCenter)

        self.label_mensaje = QLabel("", self)
        self.label_mensaje.setAlignment(Qt.AlignCenter)

        self.label_editar = QLineEdit("", self)
        self.layout_editar = QHBoxLayout()
        self.layout_editar.addStretch()
        self.layout_editar.addWidget(self.label_editar)
        self.layout_editar.addStretch()

        self.boton_jugar = QPushButton("Ingresar", self)
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

        self.show()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Return:
            self.usuario_interfaz_procesador.emit(self.label_editar.text())

    def enviar_texto(self):
        self.usuario_interfaz_procesador.emit(self.label_editar.text())

    def actualizar_ventana(self, data):
        if data:
            self.label_mensaje.setText("")
            self.label_editar.setText("")
            self.mostrar_principal_signal.emit(data)
            self.hide()
        else:
            self.label_mensaje.setText("El texto ingresado es inválido.")

    def mostrar_inicio(self):
        self.show()


class VentanaPrincipal(QWidget):

    cierre_sesion_signal = pyqtSignal()
    cierre_interfaz_procesador = pyqtSignal()

    def __init__(self, paths, *args):
        super().__init__(*args)

        self.paths = paths
        self.setGeometry(300, 100, 700, 525)
        self.setWindowTitle("Menú Principal")
        self.setWindowIcon(QIcon(path.join(*self.paths["logo"])))

        self.label_info = QLabel("Información del usuario:", self)
        self.label_info.setFont(QFont("Times", 20))
        self.label_info.setAlignment(Qt.AlignTop)

        self.label_nombre = QLabel("", self)
        self.label_nombre.setFont(QFont("Times", 16))
        self.label_nombre.setAlignment(Qt.AlignCenter)

        self.label_amigos = QLabel("", self)
        self.label_amigos.setFont(QFont("Times", 16))
        self.label_amigos.setAlignment(Qt.AlignCenter)

        self.label_personaje = QLabel("Personaje:", self)
        self.label_personaje.setFont(QFont("Times", 16))
        self.label_personaje.setAlignment(Qt.AlignCenter)

        self.img_personaje = QLabel(self)
        self.img_personaje.setAlignment(Qt.AlignCenter)

        self.label_mensaje = QLabel("", self)
        self.label_mensaje.setAlignment(Qt.AlignCenter)

        self.boton_sesion = QPushButton("Cerrar Sesión", self)
        self.boton_sesion.clicked.connect(self.cerrar_sesion)
        self.layout_boton = QHBoxLayout()
        self.layout_boton.addStretch()
        self.layout_boton.addWidget(self.boton_sesion)
        self.layout_boton.addStretch()

        self.layout_info = QVBoxLayout()
        self.layout_info.addWidget(self.label_info)
        self.layout_info.addSpacing(15)
        self.layout_info.addWidget(self.label_nombre)
        self.layout_info.addSpacing(10)
        self.layout_info.addWidget(self.label_amigos)
        self.layout_info.addSpacing(10)
        self.layout_info.addWidget(self.label_personaje)
        self.layout_info.addSpacing(-55)
        self.layout_info.addWidget(self.img_personaje)
        self.layout_info.addSpacing(15)
        self.layout_info.addLayout(self.layout_boton)
        self.layout_info.addSpacing(15)
        self.layout_info.addWidget(self.label_mensaje)
        self.layout_info.addSpacing(5)

        self.grilla_salas = QGridLayout()
        self.grilla_salas.setHorizontalSpacing(40)

        self.label_salas = QLabel("Salas:", self)
        self.label_salas.setFont(QFont("Times", 20))
        self.label_salas.setAlignment(Qt.AlignVCenter)
        self.grilla_salas.addWidget(self.label_salas, 0, 0)
        self.participantes = QLabel("Participantes:", self)
        self.participantes.setFont(QFont("Times", 20))
        self.participantes.setAlignment(Qt.AlignVCenter)
        self.grilla_salas.addWidget(self.participantes, 0, 1)

        nombres_salas = {1: "Paris", 2: "Castillo", 3: "Narnia", 4: "Temuco"}
        self.participantes_salas = {}
        for i in range(1, 5):
            label_img = QLabel(self)
            imagen = QPixmap(path.join(*self.paths["fondo_" + str(i)])).scaled(QSize(230, 110))
            label_img.setPixmap(imagen)
            boton = QPushButton("Unirse a " + nombres_salas[i], self)
            boton.clicked.connect(self.unirse_sala)
            self.cantidad = QLabel("", self)
            self.cantidad.setFont(QFont("Times", 20))
            self.cantidad.setAlignment(Qt.AlignVCenter)
            self.participantes_salas[i] = self.cantidad
            self.grilla_salas.addWidget(label_img, i * 2 - 1, 0, 2, 1)
            self.grilla_salas.addWidget(self.cantidad, i * 2 - 1, 1)
            self.grilla_salas.addWidget(boton, i * 2, 1)

        self.layout_principal = QHBoxLayout()
        self.layout_principal.addSpacing(15)
        self.layout_principal.addLayout(self.layout_info)
        self.layout_principal.addSpacing(80)
        self.layout_principal.addLayout(self.grilla_salas)
        self.layout_principal.addSpacing(15)
        self.setLayout(self.layout_principal)

    def mostrar_principal(self, data):
        path_img = self.paths["personaje"]
        path_img[3] = data["personaje"]
        imagen = QPixmap(path.join(*path_img)).scaled(QSize(190, 280))
        self.img_personaje.setPixmap(imagen)
        self.label_nombre.setText("Nombre: " + data["nombre"])
        self.label_amigos.setText("Cantidad de amigos: " + data["amigos"])
        for i in range(1, 5):
            self.participantes_salas[i].setText(str(len(data["salas"][str(i)])) + "/5")
        self.show()

    def unirse_sala(self):
        nombres_salas = {"Paris": 1, "Castillo": 2, "Narnia": 3, "Temuco": 4}
        sala = self.sender().text().replace("Unirse a ", "")
        print(sala)
        id_sala = nombres_salas[sala]
        

    def cerrar_sesion(self):
        self.cierre_sesion_signal.emit()
        self.cierre_interfaz_procesador.emit()
        self.hide()


class VentanaSala(QWidget):

    usuario_interfaz_procesador = pyqtSignal(str)
    mostrar_principal_signal = pyqtSignal(dict)

    def __init__(self, paths, *args):
        super().__init__(*args)

        self.paths = paths
        self.setGeometry(280, 200, 850, 330)
        self.entrar_sala(123)

    def entrar_sala(self, data):
        self.setWindowTitle("Menú de la Sala")

        fondo = QImage(path.join(*self.paths["fondo_" + str(1)]))
        fondo_scaled = fondo.scaled(QSize(850, 330))
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo_scaled))
        self.setPalette(palette)

        self.show()
