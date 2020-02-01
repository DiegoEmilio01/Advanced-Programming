from network import ServidorNet
from procesador import leer_parametros, ServidorProce
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    parametros = leer_parametros()

    servidor = ServidorNet(parametros["host"], parametros["port"])
    procesador = ServidorProce()

    servidor.network_procesador_signal.connect(procesador.recibir_datos)
    procesador.procesador_network_signal.connect(servidor.manejar_envio)


    app.exec()
