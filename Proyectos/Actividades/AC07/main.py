from leer_archivos import read_file
from collections import defaultdict, deque


class Ayudante:
    def __init__(self, nombre, rango, tipo, afinidad, eficiencia):
        self.nombre = nombre
        self.rango = rango
        self.tipo = tipo
        self.afinidad = int(afinidad)
        self.eficiencia = int(eficiencia)
        self.subordinados = []
        self.dict_relaciones = {
            "Coordinador": "Jefe",
            "Jefe": "Mentor",
            "Mentor": "Novato",
            "Novato": None
        }

    def agregar_ayudante(self, ayudante):
        if self.dict_relaciones[self.rango] == ayudante.rango:
            self.subordinados.append(ayudante)
        else:
            if ayudante.rango == "Mentor":
                for subordinado in self.subordinados:
                    if subordinado.tipo == ayudante.tipo:
                        subordinado.agregar_ayudante(ayudante)
                        break
            elif ayudante.rango == "Novato" and self.rango == "Coordinador":
                for subordinado in self.subordinados:
                    if subordinado.tipo == ayudante.tipo:
                        subordinado.agregar_ayudante(ayudante)
                        break
            else:
                for mentor in self.subordinados:
                    diferencia = float("inf")
                    if abs(mentor.afinidad - ayudante.afinidad) < diferencia:
                        nombre = mentor.nombre
                        diferencia = abs(mentor.afinidad - ayudante.afinidad)
                for mentor in self.subordinados:
                    if mentor.nombre == nombre:
                        mentor.agregar_ayudante(ayudante)
                        break


def grupo_mayor_eficiencia(sistema):
    # Rellenar
    pass


def imprimir_grupo(ayudante):
    cola = deque()
    cola.append(ayudante)
    lista = []
    while len(cola) > 0:
        nodo_actual = cola.popleft() 
        lista.append(nodo_actual)
        for subordinado in nodo_actual.subordinados:
            cola.append(subordinado)
    for ayudante in lista:
        print(ayudante.nombre)


def imprimir_grupo_fail(diccionario, ayudante, tipo):
    if ayudante.tipo != "Novato":
        for subordinado in ayudante.subordinados:
            diccionario = imprimir_grupo(diccionario, subordinado, tipo)
    diccionario[ayudante.rango].add(ayudante.nombre)
    if ayudante.tipo == tipo:
        for cargo in ["Coordinador", "Jefe", "Mentor", "Novato"]:
            if cargo in diccionario:
                print()
                print(cargo)
                print()
                for nombre in diccionario[cargo]:
                    print(nombre)
    return diccionario


def instanciar_cuerpo_ayudantes(ayudantes):
    # No modificar
    enzini = Ayudante(**ayudantes[0])
    for data in ayudantes[1:]:
        enzini.agregar_ayudante(Ayudante(**data))
    return enzini


if __name__ == "__main__":
    # No modificar
    ayudantes = read_file()
    cuerpo_ayudantes = instanciar_cuerpo_ayudantes(ayudantes)
    imprimir_grupo(cuerpo_ayudantes)
    grupo_mayor_eficiencia(cuerpo_ayudantes)
