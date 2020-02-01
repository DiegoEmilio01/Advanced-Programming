import menu_juego as mj
import menu_inicio as mi
import parametros as pa
import tablero as tab
import os

# El método para limpiar la consola tanto en windows como en linux me basé en:
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
os.system('cls' if os.name == 'nt' else 'clear')

usuario_valido = False
while not usuario_valido:
    usuario = input("\nIngresar nombre del jugador (ingrese 'salir' para terminar el juego): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    # Este if es para evitar un bug porque en partidas existe "ranking.txt".
    if usuario == "ranking":
        print("\nALERTA: Nombre inválido. Intente nuevamente.")
    elif ("," in usuario) or (";" in usuario) or (usuario == "")or (usuario == " "):
        print("\nALERTA: Nombre inválido. Intente nuevamente.")
    else:
        usuario_valido = True

accion = ""
salir_juego = False
if usuario == "salir":
    salir_juego = True
menu = 0
# Los volver son para volver desde los submenús.
volver_1 = False
volver_2 = False
estado = "jugar"
while not salir_juego:
    if menu == 0:
        input_valido = False
        while (not input_valido) and (not volver_1):
            lista_acciones = ["1", "2", "3", "4"]
            accion = mi.elegir_accion()
            os.system('cls' if os.name == 'nt' else 'clear')
            if (accion.isdigit() is False) or (accion not in lista_acciones):
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.\n")
            else:
                input_valido = True
        if accion == "1":
            ancho, alto, cantidad_legos = mi.partida_nueva(pa.PROB_LEGO)
            casillas_disponibles = (ancho * alto) - cantidad_legos
            if ancho not in [0, 1]:
                ta, cl = mi.creacion_tablero(ancho, alto, cantidad_legos)
                tablero_lista = ta
                coordenadas_legos = cl
                menu = 1
            if ancho == 0:
                volver_1 = False
            elif ancho == 1:
                volver_1 = True
                accion = "1"
            else:
                volver_1 = False
        elif accion == "2":
            r, ca, an, al, co, ta = mi.cargar(usuario)
            respuesta = r
            casillas_disponibles = ca
            ancho = an
            alto = al
            coordenadas_legos = co
            tablero_lista = ta
            if respuesta == "0":
                menu = 1
        elif accion == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            mi.ver_ranking()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif accion == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            salir_juego = True
    elif menu == 1:
        input_valido_2 = False
        while (not input_valido_2) and (not volver_2):
            lista_acciones_2 = ["1", "2", "3", "4"]
            accion_2 = mj.elegir_jugada(tablero_lista)
            os.system('cls' if os.name == 'nt' else 'clear')
            if (accion_2.isdigit() is False) or (accion_2 not in lista_acciones_2):
                print("\nALERTA: Ingresó un número inválido. Intente nuevamente.")
            else:
                input_valido_2 = True
        if accion_2 == "1":
            ejex, ejey = mj.elegir_casilla(ancho, alto, tablero_lista)
            if ejex not in [-2, -1]:
                ca, ta, estado = mj.desbloquear_casilla(casillas_disponibles, ejex, ejey, ancho,
                                                        alto, coordenadas_legos, tablero_lista)
                casillas_disponibles = ca
                tablero_lista = ta
            if ejex == -1:
                volver_2 = False
            elif ejex == -2:
                volver_2 = True
                accion_2 = "1"
            else:
                volver_2 = False
            if estado == "perder":
                mj.perder_partida(pa.POND_PUNT, ancho, alto, coordenadas_legos,
                                  tablero_lista, usuario, casillas_disponibles)
                menu = 0
            elif estado == "ganar":
                mj.ganar_partida(pa.POND_PUNT, ancho, alto, coordenadas_legos,
                                 tablero_lista, usuario)
                menu = 0
        if accion_2 == "2":
            menu = 0
            os.system('cls' if os.name == 'nt' else 'clear')
        elif accion_2 == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            mj.guardar_partida(usuario, casillas_disponibles, ancho, alto,
                               coordenadas_legos, tablero_lista)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif accion_2 == "4":
            guardado_valido = False
            while not guardado_valido:
                lista_opciones = ["0", "1"]
                print("\n\t Tablero:\n")
                tab.print_tablero(tablero_lista)
                print("\nEsta es la partida que se esta abandonando, ¿desea guardar?")
                print("\nElija una entre las siguientes opciones:")
                print("\n[0] Guardar.")
                print("[1] No guardar.")
                print("\nSALIENDO...")
                guardado = input("Ingrese el número aquí: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if (guardado.isdigit() is False) or (guardado not in lista_opciones):
                    print("\nALERTA: Ingresó un número inválido. Intente nuevamente.")
                else:
                    guardado_valido = True
            if guardado == "0":
                mj.guardar_partida(usuario, casillas_disponibles, ancho, alto,
                                   coordenadas_legos, tablero_lista)
            salir_juego = True
print("\nSALIENDO...")
