from menu import MenuSesion, MenuPrincipal, MenuPreparacion, MenuCompra, MenuCarrera, MenuPits
import os
from datos import cargar_datos


def main_juego():
    pilotos, vehiculos, bots, pistas = cargar_datos()
    menu_sesion = MenuSesion()
    menu_principal = MenuPrincipal()
    menu_preparacion = MenuPreparacion()
    menu_compra = MenuCompra()
    menu_carrera = MenuCarrera()
    menu_pits = MenuPits()
    os.system('cls' if os.name == 'nt' else 'clear')
    accion = "sesion"
    while accion != "salir":
        if accion in ["sesion", "volver_sesion"]:
            accion = menu_sesion.recibir_input()
            if accion == "nueva":
                accion, piloto = menu_sesion.nueva_partida(pilotos, vehiculos)
            elif accion == "cargar":
                accion, piloto = menu_sesion.cargar_partida(pilotos)
        if accion in ["principal", "volver_principal"]:
            accion = menu_principal.recibir_input()
        if accion == "guardar":
            accion = menu_principal.guardar_partida(piloto, pilotos, vehiculos)
        if accion in ["comprar", "volver_compra"]:
            accion = menu_compra.recibir_input(piloto)
            if accion != "volver_principal":
                accion = menu_compra.comprar_vehiculo(accion, piloto, vehiculos)
        if accion in ["preparacion", "volver_preparacion"]:
            accion = menu_preparacion.recibir_input(piloto, pistas)
            if accion == "elegir_auto":
                accion = menu_preparacion.elegir_vehiculo(piloto, vehiculos)
            if accion == "pista":
                accion, pista = menu_preparacion.crear_pista(piloto, pistas, vehiculos, bots)
        while accion in ["carrera", "pits"]:
            if accion == "carrera":
                accion = menu_carrera.simular_vuelta(pista)
                if accion == "terminar":
                    args = [piloto, pista, vehiculos]
                    accion, piloto, pista, vehiculos = menu_carrera.terminar_carrera(*args)
                elif accion == "carrera":
                    accion = menu_carrera.recibir_input(pista)
            if accion == "pits":
                accion, pista = menu_pits.recibir_input(pista)
    print("\nSALIENDO...")

main_juego()