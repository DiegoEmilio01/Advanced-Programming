import os
import json
import time  # Ocupe time.strftime para obtener fecha y hora


class DocengelionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Docengelion):
            return {'modelo': obj.modelo,
                    'estado': "reparacion",
                    'registro_reparacion': time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()),
                    'nucleo': obj.nucleo}
        return super().default(obj)


class Docengelion:
    def __init__(self, modelo, nucleo, *args, **kwargs):
        self.modelo = modelo
        self.nucleo = nucleo
        self.estado = 'funcional'
        self.registro_reparacion = None


def recibir_eva(ruta):
    with open(ruta, "r") as file:
        archivo = json.load(file)
    lista_evas = []
    for mecha in archivo:
        eva = Docengelion(mecha["modelo"], mecha["nucleo"])
        lista_evas.append(eva)
    return lista_evas


def reparar_eva(docengelion):
    if "Daniar" not in os.listdir("."):
        os.makedirs("Daniar")
    eva_string = json.dumps(docengelion, cls=DocengelionEncoder)
    with open(os.path.join("Daniar", "Unidad-" + str(docengelion.modelo)) + ".json", "w") as file:
        file.write(eva_string)


if __name__ == '__main__':
    try:
        dcngelions = recibir_eva('docent.json')
        if dcngelions:
            print("DANIAR200: Ha cargado las unidades Docengelion")
        try:
            for unidad in dcngelions:
                reparar_eva(unidad)
            print("DANIAR201: Se estan reparando las unidades Docengelion")
        except Exception as error:
            print(f'Error: {error}')
            print("DANIAR501: No ha podido reparar las unidades Docengelion")
    except Exception as error:
        print(f'Error: {error}')
        print("DANIAR404: No ha podido cargar las unidades Docengelion")
