# procesador.py

from PyQt5.QtCore import QObject, pyqtSignal

class Procesador(QObject):

    senal_procesar = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.senal_actualizar = None
        self.senal_procesar.connect(self.procesar_input)
    
    def es_valido(self, texto):
        caracteres_posibles = list(map(str, range(0, 10))) + [',']
        for caracter in texto:
            if caracter not in caracteres_posibles:
                return False
        return True

    def procesar_input(self, texto_input):
        texto_input = texto_input.replace(' ', '')
        if not self.es_valido(texto_input):
            self.actualizar_interfaz('Input no válido')
            return
        lista_de_numeros = [int(porcion) for porcion in texto_input.split(',')]
        numeros_ordenados = []
        while len(lista_de_numeros) > 0:
            minimo_actual = lista_de_numeros[0]
            for numero in lista_de_numeros:
                if numero < minimo_actual:
                    minimo_actual = numero
            numeros_ordenados.append(minimo_actual)
            lista_de_numeros.remove(minimo_actual)
        texto_resultado = ", ".join([str(numero) for numero in numeros_ordenados])
        self.actualizar_interfaz(texto_resultado)

    def actualizar_interfaz(self, texto):
        if self.senal_actualizar:
            self.senal_actualizar.emit(texto)