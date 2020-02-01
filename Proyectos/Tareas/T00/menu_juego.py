import tablero as tab
import os


def elegir_jugada(tablero_lista):
    print("\n\t MENÚ DE JUEGO\n")
    tab.print_tablero(tablero_lista)
    print("\nElija una entre las siguientes opciones:")
    print("\n[1] Descubrir baldosa.")
    print("[2] Volver al menú de inicio (no se guardará la partida).")
    print("[3] Guargar partida.")
    print("[4] Salir del juego.")
    accion = input("\nIngrese el número aquí: ")
    return accion


def guardar_partida(usuario, casillas_disponibles, ancho, alto,
                    coordenadas_legos, tablero_lista):
    partida_usuario = usuario + ".txt"
    ruta_partida = os.path.join("partidas", partida_usuario)
    archivo_partida = open(ruta_partida, "wt")
    print(casillas_disponibles, file=archivo_partida)
    print(ancho, file=archivo_partida)
    print(alto, file=archivo_partida)
    print(coordenadas_legos, file=archivo_partida)
    print(tablero_lista, file=archivo_partida)
    archivo_partida.close()
    print("\nGUARDANDO...")
    input("Partida guardada. Presione 'Enter' para continuar.\n")


def elegir_casilla(ancho, alto, tablero_lista):
    terminado_1 = False
    terminado_2 = False
    volver_1 = False
    volver_2 = False
    while (not terminado_1) and (not volver_1):
        print("\n\t Tablero:\n")
        tab.print_tablero(tablero_lista)
        print("\nDESBLOQUEANDO CASILLA...")
        ejey = input("Ingrese el NÚMERO de la fila (ingrese '00' para volver): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if ejey == "00":
            volver_1 = True
        elif ejey.isdigit() is False:
            print("\nALERTA: Ingresó una FILA inválida. Intente nuevamente.")
        elif int(ejey) >= alto:
            print("\nALERTA: Su FILA no está en el tablero. Intente nuevamente.")
        else:
            terminado_1 = True
            ejey = int(ejey)
    while (not terminado_2) and (not volver_1) and (not volver_2):
        print("\n\t Tablero:\n")
        tab.print_tablero(tablero_lista)
        print("\nDESBLOQUEANDO CASILLA...")
        print("El número de la fila elegida es: " + str(ejey))
        ejex = input("Ingrese la LETRA de la columna (ingrese '00' para volver): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if ejex == "00":
            volver_2 = True
        elif len(ejex) > 1:
            print("\nALERTA: Ingresó un demasiados carácteres. Intente nuevamente.")
        elif ejex.isalpha() is False:
            print("\nALERTA: Ingresó al menos un carácter no alfabético. Intente nuevamente.")
        elif ejex.isupper() is False:
            print("\nALERTA: Ingresó una LETRA en minúscula. Intente nuevamente.")
        # El método ord para transformar una letra en entero me basé en:
        # https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python
        elif (ord(ejex.lower()) - 97) >= ancho:
            print("\nALERTA: Su LETRA no está en el tablero. Intente nuevamente.")
        else:
            ejex = ord(ejex.lower()) - 97
            terminado_2 = True
            ejex = int(ejex)
    if volver_1:
        ejey = -1
        ejex = -1
    elif volver_2:
        ejex = -2
        ejey = -2
    return ejex, ejey


def desbloquear_casilla(casillas_disponibles, ejex, ejey, ancho, alto,
                        coordenadas_legos, tablero_lista):
    casilla = [ejex, ejey]
    estado = "jugar"
    if casilla in coordenadas_legos:
        estado = "perder"
    else:
        casillas_disponibles -= 1
        if casillas_disponibles == 0:
            estado = "ganar"
        # Para contar los legos me basé en un código:
        # https://stackoverflow.com/questions/33861728/python3-number-of-adjacent-mines-function
        cantidad_legos = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                mas_que_0 = False
                if (ejex + x >= 0) and (ejey + y >= 0):
                    mas_que_0 = True
                menor_que_len = False
                if (ejex + x < ancho) and (ejey + y < alto):
                    menor_que_len = True
                if  mas_que_0 and menor_que_len and ([ejex + x, ejey + y] in coordenadas_legos):
                    cantidad_legos += 1
        tablero_lista[ejey][ejex] = str(cantidad_legos)
    return casillas_disponibles, tablero_lista, estado


def perder_partida(POND_PUNT, ancho, alto, coordenadas_legos,
                   tablero_lista, usuario, casillas_disponibles):
    for legos in coordenadas_legos:
        x = legos[0]
        y = legos[1]
        tablero_lista[y][x] = "L"
    casillas_desbloqueadas = (ancho * alto) - len(coordenadas_legos) - casillas_disponibles
    puntaje = casillas_desbloqueadas * len(coordenadas_legos) * POND_PUNT
    ruta_ranking = os.path.join("partidas", "ranking.txt")
    archivo_ranking = open(ruta_ranking, "rt")
    lista_ranking = archivo_ranking.readlines()
    archivo_ranking.close()
    lista_ranking = lista_ranking[0].strip()
    lista_ranking = lista_ranking + ";" + usuario + "," + str(puntaje)
    archivo_ranking_2 = open(ruta_ranking, "wt")
    print(lista_ranking, file=archivo_ranking_2)
    archivo_ranking_2.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t ¡" + usuario + ", PERDISTE!\n")
    tab.print_tablero(tablero_lista)
    texto_3 = " puntos. Si eres de los 10 mejores tu nombre aparecerá en el ranking."
    print("\n Tu puntaje es: " + str(puntaje) + texto_3)
    input("\nPresione 'Enter' para volver al MENÚ DE INICIO.\n")
    os.system('cls' if os.name == 'nt' else 'clear')


def ganar_partida(POND_PUNT, ancho, alto, coordenadas_legos, tablero_lista, usuario):
    casillas_desbloqueadas = (ancho * alto) - len(coordenadas_legos)
    puntaje = casillas_desbloqueadas * len(coordenadas_legos) * POND_PUNT
    ruta_ranking = os.path.join("partidas", "ranking.txt")
    archivo_ranking = open(ruta_ranking, "rt")
    lista_ranking = archivo_ranking.readlines()
    archivo_ranking.close()
    lista_ranking = lista_ranking[0].strip()
    lista_ranking = lista_ranking + ";" + usuario + "," + str(puntaje)
    archivo_ranking_2 = open(ruta_ranking, "wt")
    print(lista_ranking, file=archivo_ranking_2)
    archivo_ranking_2.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t ¡" + usuario + ", GANASTE!\n")
    tab.print_tablero(tablero_lista)
    texto_3 = " puntos. Si eres de los 10 mejores tu nombre aparecerá en el ranking."
    print("\n Tu puntaje es: " + str(puntaje) + texto_3)
    input("\nPresione 'Enter' para volver al MENÚ DE INICIO.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
