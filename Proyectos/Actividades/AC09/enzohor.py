import pickle
import re


class Piloto:
    def __init__(self, nombre, alma, edad, *args, **kwargs):
        self.nombre = nombre
        self.alma = alma
        self.edad = edad

    def __setstate__(self, state):
        self.__dict__ = aumentar_sincronizacion(state)


def cargar_almas(ruta):
    with open(ruta, "rb") as file:
        archivo = pickle.load(file)
    return archivo


def aumentar_sincronizacion(estado):
    alma = estado["alma"]
    # alma = "EruGrurrEGjsasdGGasdGO"
    nueva_alma = re.sub('E[^EO]*G+[^EO]*O', '', alma)
    if estado["nombre"] == "Shinji Gonzalez":
        print(nueva_alma)
    # print(alma)
    # print(nueva_alma)
    estado["alma"] = nueva_alma
    return estado


if __name__ == '__main__':
    try:
        pilotos = cargar_almas('pilotos.magi')
        if pilotos:
            print("ENZOHOR200: Sincronizacion de los pilotos ESTABLE.")
    except Exception as error:
        print(f'Error: {error}')
        print("ENZOHOR501: CRITICO Sincronizacion de los pilotos INESTABLE")
