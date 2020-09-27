"""
Aquí debes completar las funciones de las consultas
"""
from collections import defaultdict


def resumen_actual(ayudantes, alumnos):
    print("\n---------------------------------\n")
    print("Alumnos restantes:", len(alumnos))
    piso_1 = len(ayudantes["Piso -1"])
    piso_2 = len(ayudantes["Piso -2"])
    piso_3 = len(ayudantes["Piso -3"])
    piso_4 = len(ayudantes["Piso -4"])
    total = piso_1 + piso_2 + piso_3 + piso_4
    print("Ayudantes restantes:", total)
    print("Ayudantes Piso -1:", piso_1)
    print("Ayudantes Piso -2:", piso_2)
    print("Ayudantes Piso -3:", piso_3)
    print("Ayudantes Piso -4:", piso_4)
    print("\n---------------------------------\n")
    pass


def stock_comida(alumnos):
    diccionario_comida = defaultdict(int)
    for alumno in alumnos:
        for comida in alumno.habilidades:
            diccionario_comida[comida] += 1
    lista_comida = list(diccionario_comida.items())
    return lista_comida
