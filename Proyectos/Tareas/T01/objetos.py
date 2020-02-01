from abc import ABC, abstractproperty


class Chofer:
    def __init__(self, nombre, perso, contextura, equilibrio, equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.personalidad = perso
        self.contextura = int(contextura)
        self.equilibrio = int(equilibrio)
        self._tiempo_total = 0
        self._tiempo_vuelta = 0

    @property
    def tiempo_total(self):
        return self._tiempo_total

    @tiempo_total.setter
    def tiempo_total(self, tiempo):
        self._tiempo_total += tiempo

    @tiempo_total.deleter
    def tiempo_total(self):
        del self._tiempo_total

    @property
    def tiempo_vuelta(self):
        return self._tiempo_vuelta

    @tiempo_vuelta.setter
    def tiempo_vuelta(self, tiempo):
        self._tiempo_vuelta = tiempo

    @tiempo_vuelta.deleter
    def tiempo_vuelta(self):
        del self._tiempo_vuelta


class Contrincante(Chofer):
    def __init__(self, nombre, nivel, perso, contextura, equilibrio, ex, equipo):
        super().__init__(nombre, perso, contextura, equilibrio, equipo)
        self.nivel = nivel
        self.experiencia = int(ex)

    def __str__(self):
        texto = self.nombre + "," + self.nivel + "," + self.personalidad + ","
        texto = texto + str(self.contextura) + "," + str(self.equilibrio) + ","
        texto = texto + str(self.experiencia) + "," + self.equipo
        return texto


class Piloto(Chofer):
    def __init__(self, nombre, dinero, perso, contextura, equilibrio, ex, equipo):
        super().__init__(nombre, perso, contextura, equilibrio, equipo)
        self.nivel = "jugador"
        self.en_pits = False
        self.__dinero = int(dinero)
        self.__experiencia = int(ex)
        self.__pista_elegida = ""
        self.__vehiculo_elegido = ""

    def __str__(self):
        texto = self.nombre + "," + str(self.__dinero) + "," + self.personalidad + ","
        texto = texto + str(self.contextura) + "," + str(self.equilibrio) + ","
        texto = texto + str(self.__experiencia) + "," + self.equipo
        return texto

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, cambio):
        if self.__dinero + cambio >= 0:
            self.__dinero += cambio
        else:
            print("\nALERTA: No tienes dinero suficiente.")

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, xp_ganada):
        self.__experiencia += xp_ganada

    @property
    def pista_elegida(self):
        return self.__pista_elegida

    @pista_elegida.setter
    def pista_elegida(self, pista):
        self.__pista_elegida = pista

    @pista_elegida.deleter
    def pista_elegida(self):
        del self.__pista_elegida

    @property
    def vehiculo_elegido(self):
        return self.__vehiculo_elegido

    @vehiculo_elegido.setter
    def vehiculo_elegido(self, vehiculo):
        self.__vehiculo_elegido = vehiculo

    @vehiculo_elegido.deleter
    def vehiculo_elegido(self):
        del self.__vehiculo_elegido


# Vehiculos


class Vehiculo(ABC):
    def __init__(self, nombre, dueño, chasis, carroceria, ruedas, peso):
        self.nombre = nombre
        self.dueño = dueño
        self.peso = int(peso)
        self.categoria = "rellenar dependiendo de la clase"
        self._chasis = int(chasis)
        self._chasis_carrera = int(chasis)
        self._carroceria = int(carroceria)
        self._ruedas = int(ruedas)

    @abstractproperty
    def chasis(self):
        pass

    @abstractproperty
    def chasis_carrera(self):
        pass

    @abstractproperty
    def carroceria(self):
        pass

    @abstractproperty
    def ruedas(self):
        pass


class Automovil(Vehiculo):
    def __init__(self, nombre, dueño, chasis, carroceria, ruedas, peso, motor):
        super().__init__(nombre, dueño, chasis, carroceria, ruedas, peso)
        self.categoria = "automóvil"
        self._motor = int(motor)

    def __str__(self):
        texto = self.nombre + "," + self.dueño + "," + self.categoria + ","
        texto = texto + str(self._chasis) + "," + str(self._carroceria) + ","
        texto = texto + str(self._ruedas) + "," + str(self._motor) + "," + str(self.peso)
        return texto

    @property
    def chasis(self):
        return self._chasis

    @chasis.setter
    def chasis(self, multiplcador):
        self._chasis *= multiplcador

    @property
    def chasis_carrera(self):
        return self._chasis_carrera

    @chasis_carrera.setter
    def chasis_carrera(self, cambio):
        self._chasis_carrera += cambio

    @property
    def carroceria(self):
        return self._carroceria

    @carroceria.setter
    def carroceria(self, multiplicador):
        self._carroceria *= multiplicador

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, multiplicador):
        self._ruedas *= multiplicador

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, multiplicador):
        self._motor *= multiplicador


class Motocicleta(Automovil):
    def __init__(self, nombre, dueño, chasis, carroceria, ruedas, peso, motor):
        super().__init__(nombre, dueño, chasis, carroceria, ruedas, peso, motor)
        self.categoria = "motocicleta"


class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueño, chasis, carroceria, ruedas, peso, zapatillas):
        super().__init__(nombre, dueño, chasis, carroceria, ruedas, peso)
        self.categoria = "troncomóvil"
        self._zapatillas = int(zapatillas)

    def __str__(self):
        texto = self.nombre + "," + self.dueño + "," + self.categoria + ","
        texto = texto + str(self._chasis) + "," + str(self._carroceria) + ","
        texto = texto + str(self._ruedas) + "," + str(self._zapatillas) + "," + str(self.peso)
        return texto

    @property
    def chasis(self):
        return self._chasis

    @chasis.setter
    def chasis(self, multiplcador):
        self._chasis *= multiplcador

    @property
    def chasis_carrera(self):
        return self._chasis_carrera

    @chasis_carrera.setter
    def chasis_carrera(self, cambio):
        self._chasis_carrera += cambio

    @property
    def carroceria(self):
        return self._carroceria

    @carroceria.setter
    def carroceria(self, multiplicador):
        self._carroceria *= multiplicador

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, multiplicador):
        self._ruedas *= multiplicador

    @property
    def zapatillas(self):
        return self._zapatillas

    @zapatillas.setter
    def zapatillas(self, multiplicador):
        self._zapatillas *= multiplicador


class Bicicleta(Troncomovil):
    def __init__(self, nombre, dueño, chasis, carroceria, ruedas, peso, zapatillas):
        super().__init__(nombre, dueño, chasis, carroceria, ruedas, peso, zapatillas)
        self.categoria = "bicicleta"


# Pistas


class Pista:
    def __init__(self, corredores, nombre, dificultad, largo, tipo, vueltas):
        self.nombre = nombre
        self.dificultad = int(dificultad)
        self.largo_pista = int(largo)
        self.tipo = tipo
        self.numero_vueltas = int(vueltas)
        self.corredores = corredores
        self.abandonos = []
        self._vuelta_actual = 0

    @property
    def vuelta_actual(self):
        return self._vuelta_actual

    @vuelta_actual.setter
    def vuelta_actual(self, suma_uno):
        self._vuelta_actual += suma_uno


class PistaHelada(Pista):
    def __init__(self, corredores, nombre, dificultad, largo, tipo, vueltas, hielo, **kwargs):
        super().__init__(corredores, nombre, dificultad, largo, tipo, vueltas, **kwargs)
        self.hielo = int(hielo)


class PistaRocosa(Pista):
    def __init__(self, corredores, nombre, dificultad, largo, tipo, vueltas, rocas, **kwargs):
        super().__init__(corredores, nombre, dificultad, largo, tipo, vueltas, **kwargs)
        self.rocas = int(rocas)


class PistaSuprema(PistaHelada, PistaRocosa):
    def __init__(self, corredores, nombre, dificultad, largo, tipo, vueltas, **kwargs):
        super().__init__(corredores, nombre, dificultad, largo, tipo, vueltas, **kwargs)
