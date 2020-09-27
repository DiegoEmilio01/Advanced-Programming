class ErrorPatente(Exception):
    def __init__(self, conductor):
        super().__init__()
        self.texto = "La patente " + conductor.patente +\
                     " no es la registrada para " + conductor.nombre
