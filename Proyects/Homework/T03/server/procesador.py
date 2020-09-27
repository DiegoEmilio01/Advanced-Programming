from PyQt5.QtCore import QObject, pyqtSignal
from os import path
import json


class User:
    def __init__(self, nombre, personaje, amigos):
        self.nombre = nombre
        self.personaje = personaje
        self.amigos = amigos

    def __str__(self):
        return ("Nombre: " + self.nombre + "\nPersonaje: " + self.personaje +
                "\nAmigos: " + ",".join(self.amigos))


def leer_parametros():
    with open("parametros.json", "r", encoding='utf-8') as file:
        return json.load(file)


def leer_archivos():
    with open(path.join("..", "usuarios.json"), "r", encoding='utf-8') as file:
        archivo_1 = json.load(file)
    with open(path.join("..", "amigos.json"), "r", encoding='utf-8') as file:
        archivo_2 = json.load(file)
    usuarios = {}
    for usuario in archivo_1:
        usuarios[usuario["nombre"]] = User(usuario["nombre"], usuario["personaje"],
                                           archivo_2[usuario["nombre"]])
    return usuarios


class ServidorProce(QObject):

    procesador_network_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.usuarios = leer_archivos()
        self.conectados = {}
        #self.conectados = set()
        self.salas = {1: [], 2: [], 3: [], 4: []}

    def recibir_datos(self, data):
        if data["tipo"] == "nombre_usuario":
            self.verificar_usuario(data)
        elif data["tipo"] == "cierre_sesion":
            self.cierre_sesion(data)

    def cierre_sesion(self, data):
        #self.conectados.discard(self.index_usuarios[data["id"]])
        del self.conectados[data["id"]]

    def verificar_usuario(self, data):
        if (data["contenido"] in self.usuarios and
                data["contenido"] not in self.conectados.values()):
            user = self.usuarios[data["contenido"]]
            datos = {
                "nombre": user.nombre,
                "personaje": user.personaje,
                "amigos": str(len(user.amigos)),
                "salas": self.salas
            }
            data["contenido"] = datos
            #self.conectados.add(user.nombre)
            self.conectados[data["id"]] = user.nombre
        else:
            data["contenido"] = dict()
        self.procesador_network_signal.emit(data)
