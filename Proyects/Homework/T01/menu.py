from abc import ABC, abstractmethod
from parametros import ACCIONES, AUTOMOVIL, TRONCOMOVIL, MOTOCICLETA, BICICLETA
import os
import funciones as fn
from datos import guardar_datos
import math
import random


class Menu(ABC):
    @abstractmethod
    def recibir_input(self):
        pass


class MenuSesion(Menu):
    def recibir_input(self):
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ DE SESIÓN\n\nElija una entre las siguientes opciones:")
            print("\n[0] Salir del juego.\n[1] Nueva partida.\n[2] Cargar partida.")
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["SESION"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        return ACCIONES["SESION"][accion]

    def pedir_nombre(self, lista_nombres, new):
        nombres = " - ".join(lista_nombres)
        texto = "\nIngresar nombre del jugador (ingrese '0' para volver al MENÚ DE SESIÓN): "
        usuario_valido = False
        while not usuario_valido:
            print("\n\t SUB-MENÚ DE SESIÓN")
            if new:
                print("\nLos jugadores deben llamarse diferente.\n\nNombres usados:", nombres)
                usuario = input(texto)
                os.system('cls' if os.name == 'nt' else 'clear')
                if (not usuario.replace(" ", "").isalnum()) or (usuario.replace(" ", "") == ""):
                    print("\nALERTA: Nombre inválido. Intente nuevamente.")
                elif usuario in lista_nombres:
                    print("\nALERTA: Nombre repetido. Intente nuevamente.")
                else:
                    usuario_valido = True
            else:
                print("\nNombres disponibles:", nombres)
                usuario = input(texto)
                os.system('cls' if os.name == 'nt' else 'clear')
                if (usuario not in lista_nombres) and (usuario != "0"):
                    print("\nALERTA: Nombre inválido. Intente nuevamente.")
                else:
                    usuario_valido = True
        usuario = "volver_sesion" if usuario == "0" else usuario
        return usuario

    def pedir_equipo(self):
        input_valido = False
        while not input_valido:
            print("\n\t SUB-MENÚ DE SESIÓN\n\nDebe elegir un equipo.")
            print("\nElija una entre las siguientes opciones:\n\n[0] Volver al MENÚ DE SESIÓN.")
            print("[1] Tareos.\n[2] Docencios.\n[3] Hibridos.")
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["EQUIPO"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        return ACCIONES["EQUIPO"][accion]

    def tipo_auto(self):
        input_valido = False
        while not input_valido:
            print("\n\t SUB-MENÚ DE SESIÓN\n\nElija uno entre los siguientes VEHÍCULOS:")
            print("\n[0] Volver al MENÚ DE SESIÓN.\n[1] BICICLETA\n[2] MOTOCICLETA")
            print("[3] AUTOMOVIL\n[4] TRONCOMOVIL")
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["COMPRA"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        accion = ACCIONES["COMPRA"][accion]
        accion = "volver_sesion" if accion == "volver_principal" else accion
        return accion

    def pedir_auto(self):
        auto_valido = False
        while not auto_valido:
            print("\n\t SUB-MENÚ DE SESIÓN")
            texto = "\nIngresar nombre del vehículo (ingrese '0' para volver al MENÚ DE SESIÓN): "
            auto = input(texto)
            os.system('cls' if os.name == 'nt' else 'clear')
            if (not auto.replace(" ", "").isalnum()) or (auto.replace(" ", "") == ""):
                print("\nALERTA: Nombre inválido. Intente nuevamente.")
            else:
                auto_valido = True
        auto = "volver_sesion" if auto == "0" else auto
        return auto

    def nueva_partida(self, pilotos, vehiculos):
        lista_nombres = list(pilotos.keys())
        nombre = self.pedir_nombre(lista_nombres, 1)
        if nombre == "volver_sesion":
            return "volver_sesion", "0"
        else:
            equipo = self.pedir_equipo()
            if equipo == "volver_sesion":
                return "volver_sesion", "0"
            else:
                tipo = self.tipo_auto()
                if tipo == "volver_sesion":
                    return "volver_sesion", "0"
                else:
                    nombre_auto = self.pedir_auto()
                    if nombre_auto == "volver_sesion":
                        return "volver_sesion", "0"
                    else:
                        piloto = fn.crear_piloto(nombre, equipo)
                        vehiculo = fn.crear_vehiculo(nombre_auto, nombre, tipo)
                        vehiculos[vehiculo.dueño][vehiculo.nombre] = vehiculo
                        pilotos[piloto.nombre] = piloto
                        return "guardar", piloto

    def cargar_partida(self, pilotos):
        lista_nombres = list(pilotos.keys())
        nombre = self.pedir_nombre(lista_nombres, 0)
        if nombre == "volver_sesion":
            return "volver_sesion", "0"
        else:
            piloto = pilotos[nombre]
            return "principal", piloto


class MenuPrincipal(Menu):
    def recibir_input(self):
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ PRINCIPAL\n\nElija una entre las siguientes pistas:")
            print("\n[0] Salir del juego.\n[1] Iniciar carrera.\n[2] Comprar vehículo.")
            print("[3] Guardar partida.")
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["PRINCIPAL"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        return ACCIONES["PRINCIPAL"][accion]

    def guardar_partida(self, piloto, pilotos, vehiculos):
        pilotos[piloto.nombre] = piloto
        guardar_datos(pilotos, vehiculos)
        print("GUARDANDO...")
        return "principal"


class MenuPreparacion(Menu):
    def recibir_input(self, piloto, pistas):
        lista_pistas = list(pistas.keys())
        texto = "\nIngresar nombre de la pista (ingrese '0' para volver al MENÚ PRINCIPAL): "
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ DE PREPARACIÓN")
            print("\nElija una entre las siguientes PISTAS para correr en ella:")
            print("\nNombre  -  Dificultad  -  Tipo")
            for p in lista_pistas:
                print("-", p, " - ", pistas[p].dificultad, " - ", pistas[p].tipo)
            pista = input(texto)
            os.system('cls' if os.name == 'nt' else 'clear')
            if (pista not in lista_pistas) and (pista != "0"):
                print("\nALERTA: Nombre inválido. Intente nuevamente.")
            else:
                input_valido = True
        if pista == "0":
            accion = "volver_principal"
        else:
            piloto.pista_elegida = pista
            accion = "elegir_auto"
        return accion

    def elegir_vehiculo(self, piloto, vehiculos):
        lista_nombres = list(vehiculos[piloto.nombre].keys())
        nombres = " - ".join(lista_nombres)
        texto = "\nIngresar nombre del vehículo (ingrese '0' para volver a elegir pista): "
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ DE PREPARACIÓN")
            print("\nElija uno de entre sus VEHÍCULOS para usarlo en la carrera:")
            print("\nNombres:", nombres)
            auto = input(texto)
            os.system('cls' if os.name == 'nt' else 'clear')
            i = 1
            if (auto not in lista_nombres) and (auto != "0"):
                print("\nALERTA: Nombre inválido. Intente nuevamente.")
            else:
                input_valido = True
        if auto == "0":
            piloto.pista_elegida = ""
            accion = "volver_preparacion"
        else:
            accion = "pista"
            piloto.vehiculo_elegido = auto
        return accion

    def crear_pista(self, piloto, pistas, vehiculos, contrincantes):
        pista = fn.crear_pista(piloto, pistas, vehiculos, contrincantes)
        return "carrera", pista


class MenuCompra(Menu):
    def recibir_input(self, piloto):
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ DE COMPRA")
            print("\nTu dinero actual es: $" + str(piloto.dinero))
            print("\nElija uno entre los siguientes VEHÍCULOS:\n\n[0] Volver al MENÚ PRINCIPAL.")
            print("[1] BICICLETA   \t$" + str(BICICLETA["PRECIO"]))
            print("[2] MOTOCICLETA \t$" + str(MOTOCICLETA["PRECIO"]))
            print("[3] AUTOMOVIL   \t$" + str(AUTOMOVIL["PRECIO"]))
            print("[4] TRONCOMOVIL \t$" + str(TRONCOMOVIL["PRECIO"]))
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["COMPRA"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                accion = ACCIONES["COMPRA"][accion]
                if accion == "volver_principal":
                    input_valido = True
                else:
                    if accion == "bicicleta":
                        costo = BICICLETA["PRECIO"]
                    elif accion == "motocicleta":
                        costo = MOTOCICLETA["PRECIO"]
                    elif accion == "automovil":
                        costo = AUTOMOVIL["PRECIO"]
                    else:
                        costo = TRONCOMOVIL["PRECIO"]
                    dinero = piloto.dinero
                    piloto.dinero = - costo
                    if dinero != piloto.dinero:
                        input_valido = True
        return accion

    def pedir_nombre(self, lista_nombres):
        nombres = " - ".join(lista_nombres)
        texto = "\nIngresar nombre del vehículo (ingrese '0' para volver al MENÚ DE COMPRA): "
        nombre_valido = False
        while not nombre_valido:
            print("\n\t SUB-MENÚ DE COMPRA\n\nLos vehículos deben llamarse diferente.")
            print("\nNombres usados:", nombres)
            auto = input(texto)
            os.system('cls' if os.name == 'nt' else 'clear')
            if (not auto.replace(" ", "").isalnum()) or (auto.replace(" ", "") == ""):
                print("\nALERTA: Nombre inválido. Intente nuevamente.")
            elif auto in lista_nombres:
                print("\nALERTA: Nombre repetido. Intente nuevamente.")
            else:
                nombre_valido = True
        auto = "volver_compra" if auto == "0" else auto
        return auto

    def comprar_vehiculo(self, tipo, piloto, vehiculos):
        lista_nombres = list(vehiculos[piloto.nombre].keys())
        nombre = self.pedir_nombre(lista_nombres)
        if nombre == "volver_compra":
            if tipo == "bicicleta":
                costo = BICICLETA["PRECIO"]
            elif tipo == "motocicleta":
                costo = MOTOCICLETA["PRECIO"]
            elif tipo == "automovil":
                costo = AUTOMOVIL["PRECIO"]
            else:
                costo = TRONCOMOVIL["PRECIO"]
            piloto.dinero = costo
            return "volver_compra"
        else:
            vehiculo = fn.crear_vehiculo(nombre, piloto.nombre, tipo)
            vehiculos[vehiculo.dueño][vehiculo.nombre] = vehiculo
            return "guardar"


class MenuCarrera(Menu):
    def recibir_input(self, pista):
        competidores = sorted(pista.corredores, key=fn.sort_contrincantes)
        input_valido = False
        while not input_valido:
            print("\n\t MENÚ DE CARRERA")
            print("\nVuelta", pista.vuelta_actual, "de", pista.numero_vueltas)
            print("\nOrden de los competidores:")
            print("\nN° |  Jugador\t\t|  Nivel\t|  Tiempo vuelta\t|  Tiempo total\n")
            lugar = 0
            while lugar < len(competidores):
                competidor = competidores[lugar][0]
                texto = str(lugar+1) + "° |  " + competidor.nombre + "\t|  " + competidor.nivel
                texto += "\t|  " + str(competidor.tiempo_vuelta) + " seg\t|  "
                texto += str(competidor.tiempo_total) + " seg"
                print(texto)
                lugar += 1
            print("\nCompetidores descalificados:\n")
            for perdedor in pista.abandonos:
                print("-", perdedor)
            print("\nElija una entre las siguientes opciones:\n\n[0] Continuar la carrera.")
            accion = input("[1] Ir a los Pits.\n\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if accion not in ACCIONES["CARRERA"]:
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        return ACCIONES["CARRERA"][accion]

    def simular_vuelta(self, pista):
        pista.vuelta_actual = 1
        flag = 0
        after_lap = []
        terminar = False
        for contrincante in pista.corredores:
            competidor = contrincante[0]
            auto = contrincante[1]
            velocidad_real = fn.velocidad_real(pista, contrincante)
            tiempo_vuelta = fn.lap_time(pista.largo_pista, velocidad_real)
            competidor.tiempo_total = tiempo_vuelta
            competidor.tiempo_vuelta = tiempo_vuelta
            auto.chasis_carrera = - fn.daño_vehiculo(pista, contrincante)
            probabilidad_1 = random.random()
            probabilidad_2 = fn.probabilidad_accidente(pista, contrincante)
            if probabilidad_1 <= probabilidad_2:
                auto.chasis_carrera = - auto.chasis_carrera
            if not flag:
                competidor.dinero = fn.dinero_vuelta(pista)
                if auto.chasis_carrera <= 0:
                    terminar = True
                if competidor.en_pits:
                    tiempo = fn.tiempo_pits(competidor)
                    competidor.tiempo_vuelta = competidor.tiempo_vuelta + tiempo
                    competidor.en_pits = False
            flag = 1
            if auto.chasis_carrera <= 0:
                pista.abandonos.append(competidor.nombre)
            else:
                after_lap.append([competidor, auto])
        pista.corredores = after_lap
        accion = "terminar" if terminar else "carrera"
        accion = "terminar" if pista.vuelta_actual == pista.numero_vueltas else "carrera"
        return accion

    def terminar_carrera(self, piloto, pista, vehiculos):
        os.system('cls' if os.name == 'nt' else 'clear')
        piloto, pista, vehiculos = fn.print_final(piloto, pista, vehiculos)
        os.system('cls' if os.name == 'nt' else 'clear')
        return "guardar", piloto, pista, vehiculos


class MenuPits(Menu):
    def recibir_input(self, pista):
        input_valido = False
        piloto = pista.corredores[0][0]
        if pista.corredores[0][1].categoria in ["automóvil", "motocicleta"]:
            pieza = "Motor     "
        else:
            pieza = "Zapatillas"
        while not input_valido:
            print("\n\t MENÚ DE PITS")
            print("\nTu dinero actual es: $" + str(piloto.dinero))
            print("\nElija una entre las siguientes mejoras:\n\n[0] Continuar la carrera.")
            print("[1] Chasis         $" + str(ACCIONES["PITS"]["1"]))
            print("[2] Carrocería     $" + str(ACCIONES["PITS"]["2"]))
            print("[3] Ruedas         $" + str(ACCIONES["PITS"]["3"]))
            print("[4] " + pieza + "     $" + str(ACCIONES["PITS"][pieza.replace(" ", "")]))
            accion = input("\nIngrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            # que no escriba motor o zapatilla
            if (accion not in ACCIONES["PITS"]) or (not accion.isdigit()):
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                costo = ACCIONES["PITS"][accion]
                if costo != "carrera":
                    dinero = piloto.dinero
                    piloto.dinero = - costo
                    if dinero != piloto.dinero:
                        pista = fn.comprar_mejora(accion, pista)
                        input_valido = True
                else:
                    input_valido = True
        return "carrera", pista