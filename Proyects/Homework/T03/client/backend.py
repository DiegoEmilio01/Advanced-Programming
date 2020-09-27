from PyQt5.QtCore import QObject, pyqtSignal
import os
import socket
import json
import threading
from math import ceil


def leer_parametros():
    with open("parametros.json", "r") as file:
        return json.load(file)


class ClienteNet(QObject):

    network_procesador_signal = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()
        except ConnectionRefusedError:
            print("Conexión terminada. El servidor no aceptó la conexión.")
            self.socket_client.close()
            exit()

    def connect_to_server(self):
        self.socket_client.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        while True:
            try:
                largo_total = int.from_bytes(self.socket_client.recv(4), byteorder='little')
                bloques = ceil(largo_total / 124)
                largo_bloque = 128

                dict_msg = {}
                for i in range(bloques):
                    bloque = int.from_bytes(self.socket_client.recv(4), byteorder='big')
                    dict_msg[bloque] = self.socket_client.recv(124)

                msg_codificado = bytearray()
                for bloque in range(1, bloques + 1):
                    msg_codificado.extend(dict_msg[bloque])

                if len(msg_codificado) > largo_total:
                    msg_codificado = msg_codificado[:largo_total]

                msg_serializado = msg_codificado.decode("UTF-8")
                if msg_serializado:
                    data = json.loads(msg_serializado)
                    self.network_procesador_signal.emit(data)

            except ConnectionError:  # Es decir, si el servidor se desconecta
                print(123123)
                break

    def send(self, data):
        msg_serializado = json.dumps(data)
        msg_bytes = msg_serializado.encode("UTF-8")
        largo_total = len(msg_bytes)
        little_bytes = largo_total.to_bytes(4, byteorder='little')
        self.socket_client.sendall(little_bytes)

        msg_mutable = bytearray(msg_bytes)
        bloques = ceil(largo_total / 124)
        bloque = 1
        while bloque <= bloques:
            big_bytes = bytearray(bloque.to_bytes(4, byteorder='big'))
            inicio = (bloque - 1) * 124
            if bloque == bloques:
                mensaje = msg_mutable[inicio:]
                completar_bloque = 124 - len(mensaje)
                relleno = bytearray(b"\x00") * completar_bloque
                self.socket_client.sendall(big_bytes + mensaje + relleno)
            else:
                final = bloque * 124
                mensaje = msg_mutable[inicio:final]
                self.socket_client.sendall(big_bytes + mensaje)
            bloque += 1


class ClienteProce(QObject):

    procesador_network_signal = pyqtSignal(dict)
    usuario_procesador_interfaz = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def enviar_usuario(self, texto):
        self.nombre = texto
        data = {"tipo": "nombre_usuario", "contenido": texto} # "id": self.id,
        self.procesador_network_signal.emit(data)

    def enviar_cierre(self):
        data = {"tipo": "cierre_sesion", "contenido": True}
        self.procesador_network_signal.emit(data)

    def recibir_data_network(self, data):
        if data["tipo"] == "nombre_usuario":
            self.usuario_procesador_interfaz.emit(data["contenido"])
