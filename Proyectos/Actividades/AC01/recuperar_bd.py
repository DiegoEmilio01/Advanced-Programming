from phd_pinto import DrPintoDesencriptador
'''
Debes completar la funcion recuperar archivo.
Todo lo necesario de este modulo se ejecutara en main.py
'''


def recuperar_archivo(ruta):
    print('Recuperando archivo')
    doctor = DrPintoDesencriptador()
    doctor.ruta = ruta
    lineas_desencriptadas = doctor.texto_desencriptado
    return lineas_desencriptadas


def guardar_archivo(ruta, lineas_archivo):
    with open(ruta, "w", encoding="utf-8") as file:
        for linea in lineas_archivo:
            contenido = linea + "\n"
            file.write(contenido)
    print("Archivo guardado!!")
