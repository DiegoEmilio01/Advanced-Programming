import sys
from ventanas import VentanaInicio, VentanaJuego, VentanaPausa, VentanaFinal
from tienda import VentanaTienda
from procesado import ProcesadorInicio, ProcesadorMapa, Personaje
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Ventana inicio y su procesador

    ventana_inicio = VentanaInicio()
    procesador_inicio = ProcesadorInicio()

    ventana_inicio.enviar_texto_signal.connect(procesador_inicio.procesar)
    procesador_inicio.respuesta_signal.connect(ventana_inicio.actualizar_ventana)

    # Ventana juego y procesador del mapa

    ventana_juego = VentanaJuego()
    procesador_mapa = ProcesadorMapa()

    ventana_inicio.iniciar_mapa_signal.connect(ventana_juego.mapa.iniciar_mapa)
    ventana_juego.mapa.enviar_mapa_signal.connect(procesador_mapa.leer_mapa)
    procesador_mapa.mapa_signal.connect(ventana_juego.mapa.construir_mapa)
    ventana_juego.mapa.iniciar_juego_signal.connect(ventana_juego.iniciar_juego)

    # Iniciar reloj interno

    ventana_juego.mapa.iniciar_juego_signal.connect(ventana_juego.stats.iniciar_reloj)

    # Ventana pausa

    ventana_pausa = VentanaPausa()
    ventana_juego.stats.pausar_juego_signal.connect(ventana_pausa.pausar_juego)
    ventana_juego.stats.pausar_juego_signal.connect(ventana_juego.ocultar_juego)
    ventana_juego.stats.pausar_juego_signal.connect(ventana_juego.mapa.pausar)

    ventana_pausa.despausar_juego_signal.connect(ventana_juego.stats.iniciar_reloj)
    ventana_pausa.despausar_juego_signal.connect(ventana_juego.mostrar_juego)
    ventana_pausa.despausar_juego_signal.connect(ventana_juego.mapa.despausar)

    # Ventana juego y el personaje

    ventana_tienda = VentanaTienda()

    personaje = Personaje()
    ventana_juego.enviar_datos_signal.connect(personaje.datos_mapa)
    ventana_juego.moverse_signal.connect(personaje.moverse)
    personaje.refrescar_signal.connect(ventana_juego.refrescar_pantalla)

    # Personaje reconoce tienda y le dice al inventario que envie items a tienda

    personaje.enviar_items_signal.connect(ventana_juego.inventario.enviar_items)
    personaje.enviar_items_signal.connect(ventana_juego.ocultar_juego)
    ventana_juego.inventario.dict_items_signal.connect(ventana_tienda.mostrar_tienda)

    ventana_tienda.ocultar_tienda_signal.connect(ventana_juego.stats.actualizar_dinero)
    ventana_tienda.mostrar_juego_signal.connect(ventana_juego.mostrar_juego)
    ventana_juego.stats.salir_juego_signal.connect(ventana_juego.terminar_juego)
    ventana_tienda.enviar_compra_signal.connect(ventana_juego.inventario.agregar_item)
    ventana_tienda.venta_item_signal.connect(ventana_juego.inventario.eliminar_item)

    # Personaje reconoce casa y dormir

    personaje.dormir_signal.connect(ventana_juego.stats.dormir)
    ventana_juego.stats.cambio_dia_signal.connect(ventana_juego.mapa.cambio_dia)

    # Personaje reconoce items y los recoge

    personaje.recoger_item_signal.connect(ventana_juego.mapa.recolectar_item)
    ventana_juego.mapa.item_recolectado_signal.connect(ventana_juego.inventario.agregar_item)

    # Click en el juego

    ventana_juego.enviar_click_signal.connect(ventana_juego.inventario.enviar_datos_click)
    ventana_juego.inventario.datos_click_signal.connect(ventana_juego.mapa.recibir_click)

    # Usar item

    ventana_juego.mapa.enviar_item_signal.connect(ventana_juego.inventario.gastar_item)

    # Conectar las trampas

    ventana_juego.trampa_dinero_signal.connect(ventana_juego.stats.trampa_dinero)
    ventana_juego.trampa_dinero_signal.connect(ventana_tienda.trampa_dinero)

    ventana_juego.trampa_energia_signal.connect(ventana_juego.stats.trampa_energia)

    # Energia

    ventana_juego.mapa.gastar_energia_signal.connect(ventana_juego.stats.actualizar_energia)
    personaje.recuperar_energia_signal.connect(ventana_juego.stats.actualizar_energia)

    # Final

    ventana_final = VentanaFinal()
    ventana_juego.stats.perder_partida_signal.connect(ventana_juego.ocultar_juego)
    ventana_juego.stats.perder_partida_signal.connect(ventana_final.perder_juego)

    ventana_tienda.ganar_partida_signal.connect(ventana_tienda.ocultar_tienda)
    ventana_tienda.ganar_partida_signal.connect(ventana_final.ganar_juego)

    ventana_inicio.show()
    app.exec()
