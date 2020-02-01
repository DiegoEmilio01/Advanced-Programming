import sys
from frontend import VentanaInicio, VentanaPrincipal, VentanaSala
from backend import ClienteNet, ClienteProce, leer_parametros
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    parametros = leer_parametros()

    ventana_inicio = VentanaInicio(parametros["paths"]["logo"])
    network = ClienteNet(parametros["host"], parametros["port"])
    procesador = ClienteProce()
    ventana_principal = VentanaPrincipal(parametros["paths"])
    ventana_sala = VentanaSala(parametros["paths"])

    # Señales de networking
    procesador.procesador_network_signal.connect(network.send)
    network.network_procesador_signal.connect(procesador.recibir_data_network)

    # Manejo ingreso usuario
    ventana_inicio.usuario_interfaz_procesador.connect(procesador.enviar_usuario)
    procesador.usuario_procesador_interfaz.connect(ventana_inicio.actualizar_ventana)
    ventana_inicio.mostrar_principal_signal.connect(ventana_principal.mostrar_principal)

    # Manejo cierre de sesion
    ventana_principal.cierre_sesion_signal.connect(ventana_inicio.mostrar_inicio)
    ventana_principal.cierre_interfaz_procesador.connect(procesador.enviar_cierre)

    app.exec()
