from cargar import cargar_archivos
from os import path


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []


class Pintogram:
    def __init__(self):
        self.usuarios = dict()

    def nuevo_usuario(self, id_usuario, nombre):
        usuario = Usuario(id_usuario, nombre)
        self.usuarios[id_usuario] = usuario

    def follow(self, id_seguidor, id_seguido):
        if id_seguido not in self.usuarios[id_seguidor].seguidos:
            self.usuarios[id_seguidor].seguidos.append(id_seguido)

    def cargar_red(self, ruta_red):
        raw_users = cargar_archivos(ruta_red)
        for user, name, following in raw_users:
            self.nuevo_usuario(user, name)
            for seguido in following:
                self.follow(user, seguido)
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.

    def unfollow(self, id_seguidor, id_seguido):
        if id_seguido in self.usuarios[id_seguidor].seguidos:
            self.usuarios[id_seguidor].seguidos.remove(id_seguido)
        # Método que pertmite a un usuario dejar de seguir a otro

    def mis_seguidos(self, id_usuario):
        if id_usuario in self.usuarios:
            return "\n" + str(len(self.usuarios[id_usuario].seguidos)) + " seguidor(es)."
        else:
            return "\n0 seguidores :(."
        # Método que retorna los seguidores de un usuario

    def distancia_social(self, id_usuario_1, id_usuario_2, camino=None):
        primera_recursion = True if camino is None else False
        camino = list() if camino is None else camino
        origin_user = self.usuarios[id_usuario_1]
        camino = camino + [id_usuario_1]
        if id_usuario_1 == id_usuario_2:
            if primera_recursion:
                return "\nLa distancia social es: " + str(len(camino) - 1) + "."
            else:
                return camino
        camino_corto = None
        for seguido in origin_user.seguidos:
            if seguido not in camino:
                camino_recursion = self.distancia_social(seguido, id_usuario_2, camino)
                if camino_recursion:
                    if not camino_corto or len(camino_recursion) < len(camino_corto):
                        camino_corto = camino_recursion
        if primera_recursion:
            if camino_corto is None:
                return "\nLa distancia social es: infinita."
            else:
                return "\nLa distancia social es: " + str(len(camino_corto) - 1) + "."
        else:
            return camino_corto
        # Método que retorna la "distancia social" de dos usuarios



if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "intermedio.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(pintogram.distancia_social("5", "5"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
