import socket
import json
import pickle
import re


class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9001
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.

            self.socket_cliente.connect((self.host, self.port))

            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        largo_msg = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        bytes_recibidos = bytearray()
        while len(bytes_recibidos) < largo_msg:
            largo_leer = min(200, largo_msg - len(bytes_recibidos))
            bytes_recibidos.extend(self.socket_cliente.recv(largo_leer))

        dict_msg = pickle.loads(bytes_recibidos)

        # Debe haber un string para imprimirse
        mensaje = dict_msg["mensaje"]
        # Debe haber un boolean para saber si continuar funcionando
        continuar = dict_msg["continuar"]

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar
        if input_usuario == "\\juego_nuevo":
            return {"comando": "\\juego_nuevo", "columna": 0}
        elif input_usuario == "\\salir":
            return {"comando": "\\salir", "columna": 0}
        elif bool(re.fullmatch("\\\\jugada \d+", input_usuario)):
            return {"comando": "\\jugada", "columna": input_usuario[8:]}
        else:
            return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        mensaje_serializado = json.dumps(accion)
        mensaje_codificado = mensaje_serializado.encode("UTF-8")

        largo_msg = len(mensaje_codificado).to_bytes(4, byteorder='big')
        self.socket_cliente.sendall(largo_msg + mensaje_codificado)

        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
