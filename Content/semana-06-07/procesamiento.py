# procesamiento.py

def es_valido(texto):
    caracteres_posibles = list(map(str, range(0, 10))) + [',']
    for caracter in texto:
        if caracter not in caracteres_posibles:
            return False
    return True

def procesar_input(texto_input):
    texto_input = texto_input.replace(' ', '')
    if not es_valido(texto_input):
        return 'Input no válido'
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
    return texto_resultado