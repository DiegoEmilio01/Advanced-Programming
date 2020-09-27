# Datos que vienen en los csv y orden en que se instancian

DATOS = {
    "PILOTO": ["Nombre", "Dinero", "Personalidad", "Contextura",
               "Equilibrio", "Experiencia", "Equipo"],
    "VEHICULO": ["Nombre", "Dueño", "Chasis", "Carrocería",
                 "Ruedas", "Peso", "Motor o Zapatillas"],
    "CONTRINCANTE": ["Nombre", "Nivel", "Personalidad", "Contextura",
                     "Equilibrio", "Experiencia", "Equipo"],
    "PISTA": ["Contrincantes", "Nombre", "Dificultad", "LargoPista",
              "Tipo", "NúmeroVueltas", "Hielo", "Rocas"],
    "TUPLE": ["contrincantes", "nombre", "dificultad", "largo",
              "tipo", "vueltas", "hielo", "rocas"]
}

# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 12000,
        'EFECTO': 1.15
    },
    'CARROCERIA': {
        'COSTO': 15000,
        'EFECTO': 1.2
    },
    'RUEDAS': {
        'COSTO': 2000,
        'EFECTO': 1.3
    },
    'MOTOR': {
        'COSTO': 5000,
        'EFECTO': 1.25
    },
    'ZAPATILLAS': {
        'COSTO': 1000,
        'EFECTO': 1.2
    }
}

# Diccionarios con las acciones posibles por cada menu:

ACCIONES = {
    "SESION": {
        "0": "salir",
        "1": "nueva",
        "2": "cargar"
    },
    "EQUIPO": {
        "0": "volver_sesion",
        "1": "TAREOS",
        "2": "DOCENCIOS",
        "3": "HIBRIDOS"
    },
    "PRINCIPAL": {
        "0": "salir",
        "1": "preparacion",
        "2": "comprar",
        "3": "guardar"
    },
    # Eliminar
    "PREPARACION": {
        "0": "volver_principal",
        "1": "helada",
        "2": "rocosa",
        "3": "suprema"
    },
    "COMPRA": {
        "0": "volver_principal",
        "1": "bicicleta",
        "2": "motocicleta",
        "3": "automovil",
        "4": "troncomovil"
    },
    "CARRERA": {
        "0": "carrera",
        "1": "pits"
    },
    "PITS": {
        "0": "carrera",
        "1": MEJORAS["CHASIS"]["COSTO"],
        "2": MEJORAS["CARROCERIA"]["COSTO"],
        "3": MEJORAS["RUEDAS"]["COSTO"],
        "4": 0,
        "Motor": MEJORAS["MOTOR"]["COSTO"],
        "Zapatillas": MEJORAS["ZAPATILLAS"]["COSTO"]
    }
}

# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 130,
        'MAX': 180
    },
    'CARROCERIA': {
        'MIN': 100,
        'MAX': 140
    },
    'RUEDAS': {
        'MIN': 140,
        'MAX': 180
    },
    'MOTOR': {
        'MIN': 150,
        'MAX': 200
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 300,
        'MAX': 600
    },
    "PRECIO": 50000
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 150,
        'MAX': 200
    },
    'CARROCERIA': {
        'MIN': 150,
        'MAX': 200
    },
    'RUEDAS': {
        'MIN': 70,
        'MAX': 110
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 70,
        'MAX': 120
    },
    'PESO': {
        'MIN': 500,
        'MAX': 800
    },
    "PRECIO": 100000
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 120,
        'MAX': 170
    },
    'CARROCERIA': {
        'MIN': 60,
        'MAX': 90
    },
    'RUEDAS': {
        'MIN': 100,
        'MAX': 140
    },
    'MOTOR': {
        'MIN': 100,
        'MAX': 140
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 0
    },
    'PESO': {
        'MIN': 120,
        'MAX': 200
    },
    "PRECIO": 35000
}

BICICLETA = {
    'CHASIS': {
        'MIN': 100,
        'MAX': 150
    },
    'CARROCERIA': {
        'MIN': 30,
        'MAX': 60
    },
    'RUEDAS': {
        'MIN': 170,
        'MAX': 220
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 0
    },
    'ZAPATILLAS': {
        'MIN': 20,
        'MAX': 40
    },
    'PESO': {
        'MIN': 20,
        'MAX': 40
    },
    "PRECIO": 20000
}

# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': ["precavido"]
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': ["precavido", "osado"]
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': ["osado"]
    }
}

# Numero de contrincantes en las pistas

NUMERO_CONTRINCANTES = 5

# Las constantes de las formulas

POND_EFECT_HIELO = 1.4
POND_EFECT_ROCAS = 1.5
POND_EFECT_DIFICULTAD = 0.01

# Velocidad real
VELOCIDAD_MINIMA = 100

# Velocidad intencional
EFECTO_OSADO = 1.1
EFECTO_PRECAVIDO = 0.8

# Dificultad de control del vehículo
PESO_MEDIO = 500
EQUILIBRIO_PRECAVIDO = 1.4

# Tiempo pits
TIEMPO_MINIMO_PITS = 20
VELOCIDAD_PITS = 2

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 2
BONIFICACION_OSADO = 2.5


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehículos.csv"
}

# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
