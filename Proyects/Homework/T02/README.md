# Tarea 02: DCCampo :school_satchel:


## Consideraciones generales :octocat:

* La tarea hace todo lo que debería hacer según el enunciado (menos los bonus).
* El único error se produce al cosechar choclos. Si se cosecha antes de recolectar, un sprite de choclo quedará debajo y no se podrá recolectar.
* Todo se adapta al parámetro N excepto el tamaño del personaje y el fondo de la tienda.
* El botón de pausa detiene la desaparición de items, el crecimiento de los cultivos y el reloj, sin embargo QTimer no tiene un método para continuar donde estaba. Es por esto que dichos periodos se reinician al quitar la pausa.
* La trampa de dinero funciona apretando las 3 teclas al mismo tiempo pero la de energía sólo si se aprietan bien seguido (no al mismo tiempo) y si se mantienen apretadas. Creo que esto depende del teclado utilizado.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Parte Entidades**: Implementado completamente.
    * **Parte  Jugador**: Implementada completamente.
    * **Parte  Cultivos**: Implementada completamente.
    * **Parte  Herramientas**: Implementada completamente.
    * **Parte  Aparición espontánea**: Implementada completamente.
    * **Parte  Recursos**: Implementada completamente. El despawn se detiene al pausar.
* **Parte Interfaz**: Implementado completamente.
    * **Parte  Modelación del programa**: Implementada completamente. El crecimiento y despawn son segundos reales, el reloj no.
    * **Parte  Ventanas**: Todas implementadas completamente. No se utilizó el fondo del inventario y este tiene un tamaño máximo fijo de 36, igual a la cantidad de items del sprite.
    (Estoy bastante orgulloso de poder desactivar los botones de la tienda dependiendo de la cantidad de dinero :D).
* **Parte Interacción del usuario**: Implementado completamente. Se simula entrar a la tienda o casa pero en realidad el sprite nunca las pisa para evitar errores.
* **Parte Archivos entregados**: Utilizados correctamente.
* **Parte Módulos entregados**: Utilizados correctamente.
* **Parte Funcionalidades extras**: Implementado completamente.
* **Parte Sprites**: Utilizados correctamente.
* **Parte Bonus**: No implementados
* **Parte Avance**: Sólo la carga del mapa.
* **Parte .gitignore**: Implementada completamente.

* **Los ítem en amarillo de la distribución de puntajes son**:
   1. "Adecuada separación entre back-end y front-end". En: ```procesado.py``` está el back-end y en el resto de los módulos (menos parámetros y main) está el front-end.
   2. "No se encuentran dependencias circulares". El main importa ventanas, ellas subventanas y ellas objetos.
   3. "Trabaja correctamente con todos los
   archivos  entregados". Todos los parámetros son utilizados y se logra representar los mapas.
   4. "Todos los parámetros se encuentran en un único modulo .py. Utiliza e importa correctamente parametros.py". El archivo se llama ```parametros_generales.py```.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```-> ```listdir()``` y ```path.join()```
2. ```math```-> ```floor()``` y ```ceil()```
3. ```sys```.
4. ```time``` -> ```sleep()```.
5. ```PyQt5.QtCore``` -> ```QObject```, ```pyqtSignal```, ```QSize```, ```Qt``` y ```QTimer```.
6. ```PyQt5.QtWidgets``` -> ```QWidget```, ```QLabel```, ```QHBoxLayout```, ```QGridLayout```, ```QVBoxLayout```, ```QPushButton```, ```QProgressBar```, ```QLineEdit``` y ```QApplication```.
7. ```PyQt5.QtGui``` -> ```QPixmap```, ```QFont```, ```QImage```, ```QPalette```, ```QBrush``` y ```QIcon```.
8. ```random``` -> ```random()``` y ```sample()```.
9. ```collections``` -> ```defaultdict```.


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```main.py```-> Contine la instancias de las ventanas principales y la aplicación. Conecta todas las señales.
2. ```ventanas.py```-> Contine las ventanas principales del juego (excepto tienda), ```VentanaInicio```, ```VentanaPausa```, ```VentanaJuego``` y ```VentanaFinal```.
3. ```inventario.py``` -> Contiene la subventana ```VentanaInventario``` que se instancia dentro de la ventana de juego.
4. ```mapa.py``` -> Contiene la subventana ```VentanaMapa``` que se instancia dentro de la ventana de juego.
5. ```stats.py``` -> Contiene la subventana ```VentanaStats``` que se instancia dentro de la ventana de juego.
6. ```tienda.py``` -> Contiene la ventana ```VentanaTienda``` que se instancia en el main. Se muestra al entrar con el personaje.
7. ```procesado.py``` -> Contiene ```ProcesadorInicio```, ```ProcesadorMapa``` y ```Personaje``` que corresponde a todo el back-end del juego, maneja archivos y el movimiento del personaje.
8. ```drag_drop.py```-> Contiene ```ItemDespawneable```, ```ItemDraggable``` y ```LugarDrop```. Maneja los tipos de item y el sprite de drop.
9. ```parametros_generales.py``` -> Contiene todos los parámetros necesarios para que el juego funcione (constantes y paths).



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Que siempre debajo de la puerta de la casa hay un sprite libre para poder empezar allí.
2. Recomiendo subir la energía en los parámetros generales o sino es muy fácil perder sin darse cuenta.
3. Solución de un bugg que me costó encontrar porque es una combinación de cosas. Al recoger choclos o alcachofas agrego esos puntos a pocisiones de pasto entonces se puede arar, como los choclos son permanentes causa problemas. Si uno clickea sobre un choclo (teniendo la asada) para cosechar el sprite se borra pero la planta sigue existiendo. Para solucionarlo se debe mover la línea 186 y agregar en la línea 182:

```python
        if widget.valor not in ["choclo", "alcachofa"]:
            self.pos_pastos.add(pos)
```


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. (https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5): Me basé en este código para programar el drag and drop. (drag_drop.py, línea 31).
2. (https://stackoverflow.com/questions/13184250/is-there-any-way-to-remove-a-qwidget-in-a-qgridlayout) Me basé en este código para eliminar widgets de una grilla, por ejemplo, en inventario.py, línea 65.
3. El código del personaje está basado en la ayudantía extra.
