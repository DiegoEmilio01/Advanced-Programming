import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os


class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()

    def chequear_rut(self, conductor):
        if "." in conductor.rut:
            raise ValueError('¡El rut ' + conductor.rut + ' contiene puntos!')
        if "-" != conductor.rut[-2]:
            raise ValueError('¡El rut ' + conductor.rut + ' no contiene guion!')

    def chequear_nombre(self, conductor):
        if conductor.nombre not in self.registro_oficial:
            raise ValueError('¡El conductor ' + conductor.nombre + ' no está en el registro!')

    def chequear_celular(self, conductor):
        if not conductor.celular.isdigit():
            raise ValueError('¡El celular ' + conductor.celular + ' debe contener solo dígitos!')
        if len(conductor.celular) != 9:
            raise ValueError('¡El celular ' + conductor.celular + ' no es de largo 9 dígitos!')
        if conductor.celular[0] != "9":
            raise ValueError('¡El celular ' + conductor.celular + ' no empieza con "9"!')

    def chequear_patente(self, conductor):
        if conductor.patente != self.registro_oficial[conductor.nombre]:
            raise ErrorPatente(conductor)
