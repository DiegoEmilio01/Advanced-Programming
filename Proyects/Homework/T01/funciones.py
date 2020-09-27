import math
import objetos as obj
import parametros as p
from random import randint as ri
from random import sample


def crear_piloto(nombre, equipo):
    personalidad = sample(p.EQUIPOS[equipo]["PERSONALIDAD"], 1)[0]
    contextura = ri(p.EQUIPOS[equipo]["CONTEXTURA"]["MIN"], p.EQUIPOS[equipo]["CONTEXTURA"]["MAX"])
    equilibrio = ri(p.EQUIPOS[equipo]["EQUILIBRIO"]["MIN"], p.EQUIPOS[equipo]["EQUILIBRIO"]["MAX"])
    piloto = obj.Piloto(nombre, 5000, personalidad, contextura, equilibrio, 0, equipo)
    return piloto


def crear_vehiculo(nombre, dueño, tipo):
    dict_autos = p.BICICLETA if tipo == "bicicleta" else p.AUTOMOVIL if tipo == "automovil" else 0
    if not dict_autos:
        dict_autos = p.TRONCOMOVIL if tipo == "troncomovil" else p.MOTOCICLETA
    fuerza = "MOTOR" if tipo in ["automovil", "motocicleta"] else "ZAPATILLAS"
    chasis = ri(dict_autos["CHASIS"]["MIN"], dict_autos["CHASIS"]["MAX"])
    carroceria = ri(dict_autos["CARROCERIA"]["MIN"], dict_autos["CARROCERIA"]["MAX"])
    ruedas = ri(dict_autos["RUEDAS"]["MIN"], dict_autos["RUEDAS"]["MAX"])
    peso = ri(dict_autos["PESO"]["MIN"], dict_autos["PESO"]["MAX"])
    impulso = ri(dict_autos[fuerza]["MIN"], dict_autos[fuerza]["MAX"])
    args = [nombre, dueño, chasis, carroceria, ruedas, peso, impulso]
    if tipo == "automovil":
        vehiculo = obj.Automovil(*args)
    elif tipo == "bicicleta":
        vehiculo = obj.Bicicleta(*args)
    elif tipo == "troncomovil":
        vehiculo = obj.Troncomovil(*args)
    else:
        vehiculo = obj.Motocicleta(*args)
    return vehiculo


def crear_pista(piloto, pistas, vehiculos, bots):
    nombre_pista = piloto.pista_elegida
    pista_tuple = pistas[nombre_pista]
    cantidad_bots = min(p.NUMERO_CONTRINCANTES, len(pista_tuple.contrincantes))
    lista_bots = sample(pista_tuple.contrincantes, cantidad_bots)
    lista_corredores = []
    lista_corredores.append([piloto, vehiculos[piloto.nombre][piloto.vehiculo_elegido]])
    for nombre_bot in lista_bots:
        nombre_auto = sample(vehiculos[nombre_bot].keys(), 1)[0]
        corredor_auto = [bots[nombre_bot], vehiculos[nombre_bot][nombre_auto]]
        lista_corredores.append(corredor_auto)
    args = [lista_corredores, nombre_pista, pista_tuple.dificultad, pista_tuple.largo,
            pista_tuple.tipo, pista_tuple.vueltas]
    if pista_tuple.tipo == "pista hielo":
        pista = obj.PistaHelada(*args, hielo=pista_tuple.hielo)
    elif pista_tuple.tipo == "pista rocosa":
        pista = obj.PistaRocosa(*args, rocas=pista_tuple.rocas)
    else:
        pista = obj.PistaSuprema(*args, hielo=pista_tuple.hielo, rocas=pista_tuple.rocas)
    return pista


def velocidad_real(pista, contrincante):
    rapidez_intencional = velocidad_intencional(pista, contrincante)
    control = dificultad_control(pista, contrincante)
    frio = hipotermia(pista, contrincante)
    rapidez = max(p.VELOCIDAD_MINIMA, rapidez_intencional + control + frio)
    return rapidez


def velocidad_intencional(pista, contrincante):
    competidor = contrincante[0]
    rapidez_recomendada = velocidad_recomendada(pista, contrincante)
    if competidor.personalidad == "osado":
        return rapidez_recomendada * p.EFECTO_OSADO
    else:
        return rapidez_recomendada * p.EFECTO_PRECAVIDO


def velocidad_recomendada(pista, contrincante):
    competidor = contrincante[0]
    auto = contrincante[1]
    hielo_pista = pista.hielo if pista.tipo in ["pista hielo", "pista suprema"] else 0
    rocas_pista = pista.rocas if pista.tipo in ["pista rocosa", "pista suprema"] else 0
    if auto.categoria in ["automóvil", "motocicleta"]:
        velocidad_base = auto.motor
    else:
        velocidad_base = auto.zapatillas
    velocidad = velocidad_base + (auto.ruedas - hielo_pista) * p.POND_EFECT_HIELO
    velocidad += (auto.carroceria - rocas_pista) * p.POND_EFECT_ROCAS
    velocidad += (competidor.experiencia - pista.dificultad) * p.POND_EFECT_DIFICULTAD
    return velocidad


def hipotermia(pista, contrincante):
    competidor = contrincante[0]
    hielo_pista = pista.hielo if pista.tipo in ["pista hielo", "pista suprema"] else 0
    frio = min(0, pista.vuelta_actual * (competidor.contextura - hielo_pista))
    if competidor.nivel == "jugador":
        if frio < 0:
            print("El piloto se vio afectado por el el hielo de la pista.")
    return frio


def dificultad_control(pista, contrincante):
    competidor = contrincante[0]
    auto = contrincante[1]
    if auto.categoria in ["bicicleta", "motocicleta"]:
        if competidor.personalidad == "osado":
            control = min(0, competidor.equilibrio - math.floor(p.PESO_MEDIO / auto.peso))
        else:
            division_peso = math.floor(p.PESO_MEDIO / auto.peso)
            control = min(0, (competidor.equilibrio * p.EQUILIBRIO_PRECAVIDO) - division_peso)
        if competidor.nivel == "jugador":
            if control < 0:
                print("El piloto tiene dificultad para controlar el vehículo.")
        return control
    else:
        return 0


def lap_time(largo, velocidad_real):
    tiempo = math.ceil((largo / velocidad_real))
    return tiempo


def daño_vehiculo(pista, contrincante):
    auto = contrincante[1]
    rocas_pista = pista.rocas if pista.tipo in ["pista rocosa", "pista suprema"] else 0
    daño = max(0, rocas_pista - auto.carroceria)
    return daño


def tiempo_pits(auto):
    tiempo = p.TIEMPO_MINIMO_PITS + (auto.chasis - auto.chasis_carrera) * p.VELOCIDAD_PITS
    return tiempo


def dinero_vuelta(pista):
    dinero = pista.vuelta_actual * pista.dificultad
    return dinero


def probabilidad_accidente(pista, contrincante):
    rapidez_recomendada = velocidad_recomendada(pista, contrincante)
    rapidez_real = velocidad_real(pista, contrincante)
    auto = contrincante[1]
    probabilidad_1 = max(0, (rapidez_real - rapidez_recomendada) / rapidez_recomendada)
    probabilidad_2 = math.floor((auto.chasis - auto.chasis_carrera) / auto.chasis)
    probabilidad = min(1, probabilidad_1 + probabilidad_2)
    return probabilidad


def dinero_ganar(pista):
    hielo_pista = pista.hielo if pista.tipo in ["pista hielo", "pista suprema"] else 0
    rocas_pista = pista.rocas if pista.tipo in ["pista rocosa", "pista suprema"] else 0
    dinero = pista.numero_vueltas * (pista.dificultad + hielo_pista + rocas_pista)
    return dinero


def ventaja_final(tiempo_1, tiempo_2):
    ventaja = tiempo_2 - tiempo_1
    return ventaja


def experiencia_ganar(pista, jugador, tiempo_1, tiempo_2):
    ventaja = ventaja_final(tiempo_1, tiempo_2)
    if jugador.personalidad == "precavido":
        xp = (ventaja + pista.dificultad) * p.BONIFICACION_PRECAVIDO
    else:
        xp = (ventaja + pista.dificultad) * p.BONIFICACION_OSADO
    return xp


def sort_contrincantes(contrincante):
    return contrincante[0].tiempo_total


def print_final(piloto, pista, vehiculos):
    usuario = pista.corredores[0]
    jugador = usuario[0]
    auto = usuario[1]
    if auto.chasis_carrera <= 0:
        print("\n\t PERDISTE")
        print("\nTu vehículo ha sufrido un accidente, su chasis ha llegado a 0.")
        print("\nNo puedes continuar en la carrera.")
    else:
        competidores = sorted(pista.corredores, key=sort_contrincantes)
        print("\n\t CARRERA TERMINADA")
        print("\nOrden de los competidores:")
        print("\nN° |  Jugador\t|  Nivel\t|  Tiempo total\n")
        lugar = 0
        while lugar < len(competidores):
            competidor = competidores[lugar][0]
            texto = str(lugar+1) + "° |  " + competidor.nombre + "\t|  " + competidor.nivel
            texto += "\t|  " + str(competidor.tiempo_total) + " seg"
            print(texto)
            lugar += 1
        print("\nCompetidores descalificados:\n")
        for perdedor in pista.abandonos:
            print("-", perdedor)
        if competidores[0][0].nivel == "jugador":
            if len(competidores) > 1:
                ultimo = competidores[-1][0]
                tiempo_2 = ultimo.tiempo_total
            else:
                tiempo_2 = 0
            tiempo_1 = jugador.tiempo_total
            jugador.dinero = dinero_ganar(pista)
            jugador.experiencia = experiencia_ganar(pista, jugador, tiempo_1, tiempo_2)
    jugador.pista_elegida = ""
    jugador.vehiculo_elegido = ""
    jugador.tiempo_total = 0
    tiempo = jugador.tiempo_vuelta
    jugador.tiempo_vuelta = - tiempo
    auto.chasis_carrera = (auto.chasis - auto.chasis_carrera)
    piloto = jugador
    vehiculos[jugador.nombre][auto.nombre] = auto
    input("\nPresione Enter para continuar.")
    return piloto, pista, vehiculos


def comprar_mejora(accion, pista):
    usuario = pista.corredores[0]
    contrincantes = pista[1:]
    jugador = usuario[0]
    auto = usuario[1]
    if accion == "1":
        auto.chasis = p.MEJORAS["CHASIS"]["EFECTO"]
    elif accion == "2":
        auto.carroceria = p.MEJORAS["CARROCERIA"]["EFECTO"]
    elif accion == "3":
        auto.ruedas = p.MEJORAS["RUEDAS"]["EFECTO"]
    else:
        if auto.categoria in ["automóvil", "motocicleta"]:
            auto.motor = p.MEJORAS["MOTOR"]["EFECTO"]
        else:
            auto.zapatillas = p.MEJORAS["ZAPATILLAS"]["EFECTO"]
    tiempo = tiempo_pits(auto)
    jugador.tiempo_total = tiempo
    auto.chasis_carrera = auto.chasis - auto.chasis_carrera
    pista.corredores = [[jugador, auto]] + contrincantes
    return pista
