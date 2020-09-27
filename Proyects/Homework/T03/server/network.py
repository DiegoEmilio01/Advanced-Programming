from PyQt5.QtCore import QObject, pyqtSignal
import socket
import threading
import json
from math import ceil


# print(socket.gethostname())
# print(socket.gethostbyname("diegodebian"))


class ServidorNet(QObject):

    network_procesador_signal = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()

        self.host = host
        self.port = port
        self.clientes = dict()
        self.dict_clientes = dict()
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()

    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        print("Servidor aceptando conexiones...")

        id_cliente = 0
        while True:
            try:
                client_socket, _ = self.socket_server.accept()
                self.clientes[id_cliente] = client_socket
                listening_client_thread = threading.Thread(
                    target=self.listen_client_thread,
                    args=(client_socket, id_cliente),
                    daemon=True)
                listening_client_thread.start()
                id_cliente += 1
            except ConnectionError:
                print("Ocurrió un error de conexión.")

    def listen_client_thread(self, client_socket, id_cliente):
        print("Servidor conectado a un nuevo cliente...")

        while True:
            try:
                largo_total = int.from_bytes(client_socket.recv(4), byteorder='little')
                bloques = ceil(largo_total / 124)
                largo_bloque = 128

                dict_msg = {}
                for i in range(bloques):
                    bloque = int.from_bytes(client_socket.recv(4), byteorder='big')
                    dict_msg[bloque] = client_socket.recv(124)

                msg_codificado = bytearray()
                for bloque in range(1, bloques + 1):
                    msg_codificado.extend(dict_msg[bloque])

                if len(msg_codificado) > largo_total:
                    msg_codificado = msg_codificado[:largo_total]

                msg_serializado = msg_codificado.decode("UTF-8")
                if msg_serializado:
                    data = json.loads(msg_serializado)
                    data["id"] = id_cliente
                    self.network_procesador_signal.emit(data)

            except ConnectionError:  # Es decir, si el cliente se desconecta
                print(1)
                del self.clientes[id_cliente]
                break

    def manejar_envio(self, data):
        if data["tipo"] == "nombre_usuario":
            self.enviar(data, False)

    def enviar(self, data, enviar_a_todos):
        msg_serializado = json.dumps(data)
        msg_bytes = msg_serializado.encode("UTF-8")
        largo_total = len(msg_bytes)
        little_bytes = largo_total.to_bytes(4, byteorder='little')
        try:
            if enviar_a_todos:
                pass
            else:
                self.clientes[data["id"]].sendall(little_bytes)

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
                    if enviar_a_todos:
                        pass
                    else:
                        self.clientes[data["id"]].sendall(big_bytes + mensaje + relleno)
                else:
                    final = bloque * 124
                    mensaje = msg_mutable[inicio:final]
                    if enviar_a_todos:
                        pass
                    else:
                        self.clientes[data["id"]].sendall(big_bytes + mensaje)
                bloque += 1
        except ConnectionResetError:
            del self.clientes[data["id"]]
            print('Error de conexion con cliente')
        except ConnectionAbortedError:
            del self.clientes[data["id"]]
            print('Error de conexion con cliente')
        except IndexError:
            print('Ya se ha eliminado el cliente del diccionario')
