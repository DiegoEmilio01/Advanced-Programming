"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""
from collections import deque, defaultdict, namedtuple

"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    Alumno = namedtuple('Alumno', ['nombre', 'habilidades'])
    stack_alumnos = []
    with open(ruta_archivo_alumnos, 'rt', encoding='utf-8') as file:
        for lineas in file:
            lista_alumno = lineas.strip().split(";")
            nombre_alumno = lista_alumno[0]
            habilidades = lista_alumno[1].split(",")
            set_habilidades = set(habilidades)
            alumno = Alumno(nombre_alumno, set_habilidades)
            stack_alumnos.append(alumno)
    return stack_alumnos


def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    Ayudante = namedtuple('Ayudante', ['nombre', 'debilidades', "comiendo"])
    diccionarios_pisos = defaultdict(deque)
    with open(ruta_archivo_ayudantes, 'rt', encoding='utf-8') as file:
        for lineas in file:
            lista_ayudante = lineas.strip().split(";")
            nombre_ayudante = lista_ayudante[0]
            piso_ayudante = DICT_PISOS[lista_ayudante[1]]
            debilidades = lista_ayudante[2].split(",")
            set_debilidades = set(debilidades)
            ayudante = Ayudante(nombre_ayudante, set_debilidades, [])
            diccionarios_pisos[piso_ayudante].append(ayudante)
    return diccionarios_pisos
