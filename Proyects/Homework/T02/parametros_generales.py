from os.path import join

N = 32
VEL_MOVIMIENTO = 8  # divisor de N

ENERGIA_JUGADOR = 30
ENERGIA_DORMIR = -15  # "-" porque el resto de energias se consideran gastos

PROB_ARBOL = 60 / 100
PROB_ORO = 70 / 100  # Mas alta porque de no ocurrir arbol, puede ocurrir oro, es dependiente.

DURACION_MINUTO = 0.2  # en segundos
DURACION_LENA = 45
DURACION_ORO = 30

PATH_LOGO = join("sprites", "otros", "logo.png")
PATH_INVENTARIO = join("sprites", "otros", "invetary_template.jpg")
PATH_FONDO_MAPA = join("sprites", "otros", "window_template.jpg")

MONEDAS_INICIALES = 12
DINERO_TRAMPA = 500

MAX_ITEMS = 36

PATHS_MOV = {
    ("D", 1): join("sprites", "personaje", "down_1.png"),
    ("D", 2): join("sprites", "personaje", "down_2.png"),
    ("D", 3): join("sprites", "personaje", "down_3.png"),
    ("D", 4): join("sprites", "personaje", "down_4.png"),
    ("L", 1): join("sprites", "personaje", "left_1.png"),
    ("L", 2): join("sprites", "personaje", "left_2.png"),
    ("L", 3): join("sprites", "personaje", "left_3.png"),
    ("L", 4): join("sprites", "personaje", "left_4.png"),
    ("R", 1): join("sprites", "personaje", "right_1.png"),
    ("R", 2): join("sprites", "personaje", "right_2.png"),
    ("R", 3): join("sprites", "personaje", "right_3.png"),
    ("R", 4): join("sprites", "personaje", "right_4.png"),
    ("U", 1): join("sprites", "personaje", "up_1.png"),
    ("U", 2): join("sprites", "personaje", "up_2.png"),
    ("U", 3): join("sprites", "personaje", "up_3.png"),
    ("U", 4): join("sprites", "personaje", "up_4.png")
}

PATH_TIENDA = {
    "azada": join("sprites", "otros", "hoe.png"),
    "hacha": join("sprites", "otros", "axe.png"),
    "seed_c": join("sprites", "cultivos", "choclo", "seeds.png"),
    "seed_a": join("sprites", "cultivos", "alcachofa", "seeds.png"),
    "alcachofa": join("sprites", "recursos", "artichoke.png"),
    "choclo": join("sprites", "recursos", "corn.png"),
    "rama": join("sprites", "recursos", "wood.png"),
    "oro": join("sprites", "recursos", "gold.png"),
    "ticket": join("sprites", "otros", "ticket.png")
}

PATH_MAPA = {
    "O": join("sprites", "mapa", "tile006.png"),
    "R": join("sprites", "mapa", "tile030.png"),
    "C": join("sprites", "mapa", "tile031.png"),
    "H": join("sprites", "mapa", "house.png"),
    "T": join("sprites", "mapa", "store.png"),
    "A": join("sprites", "otros", "tree.png"),
    "oro": join("sprites", "recursos", "gold.png"),
    "rama": join("sprites", "recursos", "wood.png"),
    "alcachofa": join("sprites", "recursos", "artichoke.png"),
    "choclo": join("sprites", "recursos", "corn.png")
}
