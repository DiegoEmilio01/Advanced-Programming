import math
import random
import os
import tablero as tab


def elegir_accion():
    print("\n\t MENÚ DE INICIO")
    print("\nElija una entre las siguientes opciones:")
    print("\n[1] Partida nueva.")
    print("[2] Cargar partida.")
    print("[3] Ver ranking.")
    print("[4] Salir.")
    accion = input("\nIngrese el número aquí: ")
    return accion


def partida_nueva(PROB_LEGO):
    terminado_1 = False
    terminado_2 = False
    texto_1 = "del tablero, un entero perteneciante a [3,15] (ingrese '0' para volver): "
    volver_1 = False
    volver_2 = False
    while (not terminado_1) and (not volver_1):
        print("\nCREANDO PARTIDA...")
        ancho = input("Ingrese el ANCHO " + texto_1)
        os.system('cls' if os.name == 'nt' else 'clear')
        if ancho == "0":
            volver_1 = True
        elif ancho.isdigit() is False:
            print("\nALERTA: Ingresó un ANCHO inválido. Intente nuevamente.")
        elif int(ancho) < 3 or int(ancho) > 15:
            print("\nALERTA: Su ANCHO no está en el rango especificado. Intente nuevamente.")
        else:
            terminado_1 = True
            ancho = int(ancho)
    while (not terminado_2) and (not volver_1) and (not volver_2):
        print("\nCREANDO PARTIDA...")
        alto = input("Ingrese el ALTO " + texto_1)
        os.system('cls' if os.name == 'nt' else 'clear')
        if alto == "0":
            volver_2 = True
        elif alto.isdigit() is False:
            print("\nALERTA: Ingresó un ALTO inválido. Intente nuevamente.")
        elif int(alto) < 3 or int(alto) > 15:
            print("\nALERTA: Su ALTO no está en el rango especificado. Intente nuevamente.")
        else:
            terminado_2 = True
            alto = int(alto)
    if volver_1:
        ancho = 0
        alto = 0
        cant_legos = 0
    elif volver_2:
        ancho = 1
        alto = 1
        cant_legos = 1
    else:
        cant_legos = math.ceil(ancho * alto * PROB_LEGO)
        # print("\nSu tablero posee " + str(cant_legos) + " legos escondidos.\n")
    return ancho, alto, cant_legos


def creacion_tablero(ancho, alto, cant_legos):
    num_legos = 0
    coordenadas_legos = []
    while num_legos < cant_legos:
        x = random.randint(0, ancho - 1)
        y = random.randint(0, alto - 1)
        ubicacion = [x, y]
        if ubicacion not in coordenadas_legos:
            coordenadas_legos.append(ubicacion)
            num_legos += 1
    tablero_lista = []
    for filas in range(0, alto):
        fila = []
        for columnas in range(0, ancho):
            fila.append(" ")
        tablero_lista.append(fila)
    return tablero_lista, coordenadas_legos


def ver_ranking():
    ruta_ranking = os.path.join("partidas", "ranking.txt")
    archivo_ranking = open(ruta_ranking, "rt")
    lista_ranking = archivo_ranking.readlines()
    archivo_ranking.close()
    lista_ranking = lista_ranking[0].strip().split(";")
    lista_desordenada = []
    for usuario in lista_ranking:
        lista_usuario = usuario.split(",")
        lista_formato = [lista_usuario[0], int(lista_usuario[1])]
        lista_desordenada.append(lista_formato)
    lista_ordenada = sorted(lista_desordenada, key=lambda usuario: usuario[1], reverse=True)
    print("\n\t RANKING DE LOS 10 MEJORES")
    print("\n    Jugador - Puntaje")
    lugar_jugador = 0
    while (lugar_jugador < 10) and (lugar_jugador < len(lista_ordenada)):
        jugador = lista_ordenada[lugar_jugador]
        if lugar_jugador == 9:
            espacio = "° "
        else:
            espacio = "°  "
        print(str(lugar_jugador+1) + espacio + jugador[0] + " - " + str(jugador[1]))
        lugar_jugador += 1
    input("\nPresione 'Enter' para continuar.\n")

def cargar(usuario):
    archivos = os.listdir("partidas")
    partida_nueva = usuario + ".txt"
    respuesta = "0"
    if partida_nueva in archivos:
        ruta_partida = os.path.join("partidas", partida_nueva)
        archivo_partida = open(ruta_partida, "rt")
        lineas_partida = archivo_partida.readlines()
        archivo_partida.close()
        casillas_disponibles = int(lineas_partida[0].strip())
        ancho = int(lineas_partida[1].strip())
        alto = int(lineas_partida[2].strip())
        coordenadas_legos = lineas_partida[3].strip()
        coordenadas_legos = coordenadas_legos.replace("[[", "")
        coordenadas_legos = coordenadas_legos.replace("]]", "")
        coordenadas_legos = coordenadas_legos.split("], [")
        nuevas_coord = []
        for coord in coordenadas_legos:
            coord = coord.split(", ")
            nueva_coord = [int(coord[0]), int(coord[1])]
            nuevas_coord.append(nueva_coord)
        tablero_lista = lineas_partida[4].strip()
        tablero_lista = tablero_lista.replace("[[", "")
        tablero_lista = tablero_lista.replace("]]", "")
        tablero_lista = tablero_lista.split("], [")
        nuevo_tablero = []
        for fila in tablero_lista:
            fila = fila.replace("'", "")
            nueva_fila = fila.split(", ")
            nuevo_tablero.append(nueva_fila)
        respuesta_valida = False
        while not respuesta_valida:
            lista_opciones = ["0", "1"]
            print("\n\t Tablero:\n")
            tab.print_tablero(nuevo_tablero)
            print("\nEsta es la partida que se esta cargando.")
            print("\nElija una entre las siguientes opciones:")
            print("\n[0] Confirmar carga.")
            print("[1] No cargar esta partida (volver al menú).")
            print("\nCARGANDO...")
            respuesta = input("Ingrese el número aquí: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if (respuesta.isdigit() is False) or (respuesta not in lista_opciones):
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.")
            else:
                respuesta_valida = True
    elif respuesta == "1":
        print("\nPartida no cargada.")
        casillas_disponibles = 0
        ancho = 0
        alto = 0
        nuevas_coord = 0
        nuevo_tablero = 0
    else:
        print("\nALERTA: No existe partida guardada para este jugador.")
        respuesta = "1"
        casillas_disponibles = 0
        ancho = 0
        alto = 0
        nuevas_coord = 0
        nuevo_tablero = 0
    return respuesta, casillas_disponibles, ancho, alto, nuevas_coord, nuevo_tablero
