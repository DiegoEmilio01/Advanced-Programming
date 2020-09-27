def reparar_comunicacion(ruta):
    with open(ruta, 'rb') as bytes_file:
        bytes_leidos = bytes_file.read()
        btarray = bytearray(bytes_leidos)
    bytes_buenos = bytearray(b"")
    for i in range(0, len(btarray), 16):
        chunk = bytearray(btarray[i:i+16])
        piv = True
        for byte in chunk:
            if piv:
                pivote = byte
                piv = False
            else:
                if byte < pivote:
                   bytes_buenos.append(byte)

    with open('Docengelion.bmp', 'wb') as bytes_file:
        bytes_file.write(bytes_buenos)

if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")