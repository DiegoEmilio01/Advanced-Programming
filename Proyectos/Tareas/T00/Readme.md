# Tarea 00: LegoSweeper :school_satchel:

## Consideraciones generales :octocat:

* El juego empieza y lo primero que pide es el usuario en un sub-menú. Para que no ocurran bugs a la hora de guardar/cargar algunos carácteres o nombres no están permitidos.
* La pantalla se limpia cada vez que se actualiza aunque no se haya pedido. Esto funciona en Linux y Windows, se probó en ambos.
* Luego entra al MENÚ DE INICIO. Ahí el jugador puede hacer todas las acciones solicitadas. Puede cargar una partida siempre que haya guardado una antes a su nombre.
* Al crear patrida en "Partida nueva" entra a un primer sub-menú donde se elige el ancho del tablero y después en otro sub-menú donde se elige alto. Como son sub-menús se implementó una forma de "volver", desde el ancho al MENÚ DE INICIO y desde el alto al ancho. Se corroboró que la variables se resetearan y al hacer combinaciones y recorrer menús y sub-menús no se buggueara.
* Dejé un print como comentario, este muestra la cantidad de legos lo que me ayudó durante la programación. Puede que ayude en la corrección, pero después implementé la limpieza de terminal y es probable que ya no se muestre correctamente.
* El ranking también es técnicamente un sub-menú pero sólo se puede interactuar con él para salir de ese menú.
* Las alertas avisan al usuario que está haciendo mal y demuestran las cosas que consideré para que sea a prueba de inputs no esperados.
* El MENÚ DE JUEGO es practicamente igual al MENÚ DE INICIO. Lo mismo sucede con los sub-menús al desbloquear una baldosa comparados con los de ingresar tamaños de tablero.
* Los sub-menús de ganar y perder funcionan igual que el de ranking.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Parte Menús**:
    * **Parte  Menú de inicio**: Hecha completa.
    * **Parte  Menú de juego**: Me faltó imprimir un mensaje de alerta cuando se intenta desbloquear baldosa que ya estába desbloqueada si a eso se refiere el enunciado con "entregar una respuesta apropiada".
* **Parte Reglas**: Hecha completa.
* **Parte Partida**:
    * **Parte Crear**: Hecha completa.
    * **Parte Guardar**: Hecha completa.
    * **Parte Cargar**: Hecha completa.
* **Parte Puntajes**: Hecha completa.
* **Parte Archivos entregados**: Utilizados correctamente.
* **Parte Bonus**: No hecho.
* **Los ítem en amarillo de la distribución de puntajes están en**:
    1. "La cantidad de Legos por tablero se calcula de forma correcta". En: ```menu_inicio.py```, ```partida_nueva()``` en línea 59.
    2. "El puntaje final se calcula de forma correcta". En: ```menu_juego.py```, ```perder_partida()``` en las líneas 117 y 118, y ```ganar_partida()``` en las líneas 138 y 139.
    3. "Se utilizan los parámetros entregados dentro del programa, y se importa el módulo de forma correcta". En: ```main.py``` en la línea 3, y se utilizan como parámetros de funciones en las líneas 44, 100 y 104.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```math```-> ```ceil()```
2. ```os```-> ```system('cls' if os.name == 'nt' else 'clear')```, ```path.join()```, ```listdir()```
3. ```random```-> ```randint()```
4. ```tablero```-> ```print_tablero()```
5. ```parametros```-> ```PROB_LEGO```, ```POND_PUNT```


### Librerías propias
Por otro lado, los módulos que fueron creados son los siguientes:

1. ```menu_inicio```-> Contine a ```elegir_accion()```, ```partida_nueva()```, ```creacion_tablero()```, ```ver_ranking()``` y ```cargar()```. Todas las funciones que participan en el MENÚ DE INICIO y en sus sub-menús.
2. ```menu_juego```-> Contine a ```elegir_jugada()```, ```guardar_partida()```, ```elegir_casilla()```, ```desbloquear_casilla()``` , ```perder_partida()``` y ```ganar_partida()```. Todas las funciones que participan en el MENÚ DE JUEGO y en sus sub-menús.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El juego se inicia y sólo pide nombre al usuario una vez, antes de poder crear partida o cargar una. Para ingresar otro nombre se debe salir del juego y volver a entrar. Esto se hizo así porque dada la cantidad de condiciones y sub-menús a manejar era una variable menos de la que preocuparme al construir la lógica detrás y así concentrarme en que los nombres no causaran problemas. Además, no es tanto más engorroso volver a iniciar para cambiar el nombre.
2. En vez de guardar los puntajes en "puntajes.txt" los guardé en "partidas/ranking.txt" porque la función ranking la programé primero y como almacenaba todos los puntajes no le cambie el nombre al programar perder y ganar.
3. El enunciado decía guardar todo el historial de puntajes así que en "partidas/ranking.txt" dejé Daniel (mi hermano) y Jaime (mi papá) que probaron el juego (aparte de mí).

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de (links también citados dentro el código):
1. (https://stackoverflow.com/questions/2084508/clear-terminal-in-python): esto me permitió borrar la consola y que todo quede más agradable a la vista. Está implementado en todos los módulos y funciona tanto en Windows como Linux. Ej: ```main.py``` en la línea 9.
2. (https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python): esto me permitió transformar la letra de una coordenada alfabética en una numérica y no tener que tranfformar las 16 letras (del largo máximo). Se implementó en ```menu_juego.py```, en la función ```elegir_casilla()``` en la línea 69.
3. (https://stackoverflow.com/questions/33861728/python3-number-of-adjacent-mines-function): esto me facilitó el contar la cantidad de legos alrededor de una baldosa. Fue adaptado. Está implementado en ```menu_juego.py```, en la función ```desbloquear_casilla()``` en la línea 84.
