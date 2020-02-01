from parametros import PATHS, DATOS
from objetos import Piloto, Automovil, Motocicleta, Troncomovil, Bicicleta, Contrincante
from collections import namedtuple, defaultdict


def cargar_datos():
    print('CARGANDO DATOS...')
    vehiculos = cargar_vehiculos()
    pilotos = cargar_pilotos()
    contrincantes = cargar_contrincantes()
    pistas = cargar_pistas()
    return pilotos, vehiculos, contrincantes, pistas


def cargar_pilotos():
    pilotos = {}
    with open(PATHS["PILOTOS"], 'rt', encoding='utf-8') as file:
        flag = 0
        for lineas in file:
            lista_piloto = lineas.strip().split(",")
            if flag:
                piloto_orden = [lista_piloto[orden.index(dato)] for dato in DATOS["PILOTO"]]
                piloto = Piloto(*piloto_orden)
                pilotos[piloto.nombre] = piloto
            else:
                orden = lista_piloto
            flag = 1
    return pilotos


def cargar_vehiculos():
    vehiculos = defaultdict(dict)
    with open(PATHS["VEHICULOS"], 'rt', encoding='utf-8') as file:
        flag = 0
        for lineas in file:
            lista_auto = lineas.strip().split(",")
            if flag:
                vehiculo_orden = [lista_auto[orden.index(d)] for d in DATOS["VEHICULO"]]
                if "automóvil" in lista_auto:
                    vehiculo = Automovil(*vehiculo_orden)
                elif "bicicleta" in lista_auto:
                    vehiculo = Bicicleta(*vehiculo_orden)
                elif "troncomóvil" in lista_auto:
                    vehiculo = Troncomovil(*vehiculo_orden)
                else:
                    vehiculo = Motocicleta(*vehiculo_orden)
                vehiculos[vehiculo.dueño][vehiculo.nombre] = vehiculo
            else:
                orden = lista_auto
                print(orden)
            flag = 1
    return vehiculos


def cargar_contrincantes():
    contrincantes = {}
    with open(PATHS["CONTRINCANTES"], 'rt', encoding='utf-8') as file:
        flag = 0
        for lineas in file:
            lista_bot = lineas.strip().split(",")
            if flag:
                bot_orden = [lista_bot[orden.index(dato)] for dato in DATOS["CONTRINCANTE"]]
                bot = Contrincante(*bot_orden)
                contrincantes[bot.nombre] = bot
            else:
                orden = lista_bot
            flag = 1
    return contrincantes


def cargar_pistas():
    pistas = {}
    Pista_Nt = namedtuple("Pista", DATOS["TUPLE"])
    with open(PATHS["PISTAS"], 'rt', encoding='utf-8') as file:
        flag = 0
        for lineas in file:
            lista_pista = lineas.strip().split(",")
            if flag:
                pista_orden = [lista_pista[orden.index(dato)] for dato in DATOS["PISTA"]]
                pista_desglosada = [d.split(";") if ";" in d else d for d in pista_orden]
                pista = Pista_Nt(*pista_desglosada)
                pistas[pista.nombre] = pista
            else:
                orden = lista_pista
            flag = 1
    return pistas


def guardar_datos(pilotos, vehiculos):
    guardar_pilotos(pilotos)
    guardar_vehiculos(vehiculos)


def guardar_pilotos(pilotos):
    with open(PATHS["PILOTOS"], 'w', encoding='utf-8') as file:
        linea = "Nombre,Dinero,Personalidad,Contextura,Equilibrio,Experiencia,Equipo\n"
        file.write(linea)
        for piloto in pilotos.values():
            linea = str(piloto) + "\n"
            file.write(linea)


def guardar_vehiculos(vehiculos):
    lista_vehiculos = [elemento for elemento in vehiculos.values()]
    with open(PATHS["VEHICULOS"], 'w', encoding='utf-8') as file:
        linea = "Nombre,Dueño,Categoría,Chasis,Carrocería,Ruedas,Motor o Zapatillas,Peso\n"
        file.write(linea)
        for dict_vehiculo in lista_vehiculos:
            for vehiculo in dict_vehiculo.values():
                linea = str(vehiculo) + "\n"
                file.write(linea)
