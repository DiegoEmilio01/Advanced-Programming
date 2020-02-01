# Tarea 01: Initial P :school_satchel:


## Consideraciones generales :octocat:

* El flujo del juego se aprecia en la función ```main_juego()```, esta función se encarga de llamar a todas las demás para ordenar el juego. Instancia los menús y, dependiendo de los inputs, los alterna entre ellos para que el usuario pueda cambiarse de uno a otro con facilidad.
* La pantalla se limpia cada vez que se actualiza aunque no se haya pedido. Esto funciona en Linux y Windows, se probó en ambos.
* Al principio los menú son más prolijos en formato por la falta de tiempo al programar los que el usuario se encuentra después.
* Se puede volver siempre, excepto al MENÚ DE SESIÓN y para salir de la carrera esta debe terminarse. Los SUB-MENÚS fueron necesarios para poder interactuar con el usuario y que esta fuera a prueba de errores. Desde ellos se puede volver siempre y sólo al menú anterior. Por ejemplo, si un menú tiene 2 sub-menús, el segundo vuelve al menú (no al sub-menú anterior) y se resetean los valores ingresados anteriormente.
* En general se maneja mediante inputs numericos, pero como los pilotos o vehículos pueden ser demasiados opté por que ingresaran el nombre exacto. Sí, para las pistas y nombres raros y largos predeterminados empeora la experiencia de juego :(.
* Los pilotos pueden ganar experiencia no entera, algo no considerado a la hora de instanciarlos al iniciar el juego. Si ya jugó una carrera puede dar error.
* **Importante** Respecto al MENÚ DE LOS PITS , en el módulo ```funciones.py```, en la línea 223 debe decir ```contrincantes = pista.corredores[1:]``` para que funcione lo descrito en el siguiente punto a esto respecto a dicho menú.

### Cosas implementadas y no implementadas :white_check_mark: :x:


* **Parte Menús**: Todos los menú son a prueba de errores en inputs (los errores por combinaciónes de inputs son causa de errores en el procesado de la información en partes que se explican más adelante).
    * **Parte  Menú de sesión**: Implementada completamente. Considera los cambios de columnas en los csv.
    * **Parte  Menú principal**: Implementada completamente.
    * **Parte  Menú de compra de vehículos**: Implementada completamente.
    * **Parte  Menú de preparación de carrera**: Implementada completamente.
    * **Parte  Menú de carrera**: Los corredores que lleguen a tener chasis 0 por accidentes o rocas se eliminan correctamente pero si el piloto es eliminado la carrera notermina bien. Al terminar una carrera la pista no se resetea bien y los jugadores quedan con el tiempo acumulado de la carrera anterior, para evitar esto se debe iniciar el juego de nuevo. El final al terminar la carrera se imprime bien. 
    * **Parte  Menú de los pits**: El costo del motor y zatatillas quedó erroneamente asignado a 0, por lo que no se detecta compra, así que esa mejora no se puede realizar. El resto de mejoras funcionan según lo pedido, se pondera el efecto y se guardan correctamente. Un bug aparece al aplicar los efectos porque los ponderadores que probé en ```parámetros.py``` pueden dar valores no enteros, entonces, al instanciar vehículos en el siguiente inicio dará error. El chasis se repara sólo si se compra una mejora, además, el tiempo en pits también sólo se suma si se compra una mejora, sino es como si nunca hubiese pasado por los pits.
* **Parte Archivos entregados**: Utilizados correctamente. Sólo los parámetros no enteros dan los problemas ya descritos, est no se alcanzó a probar debido al tiempo.
* **Parte Bonus**: Buenas prácticas implementado completamente. Power ups no implementado.
* **Parte Diagrama**: Hecha completa.
* **Parte .gitignore**: Implementada completamente.

* **Los ítem en amarillo de la distribución de puntajes están en**:
   1. "Los vehículos están bien modelados". En: ```objetos.py``` entre las líneas 115 y 258.
   2. "Las pistas están bien modeladas". En: ```objetos.py``` entre las líneas 264 y 298.
   3. "Los pilotos están bien modelados". En: ```objetos.py``` entre las líneas 4 y 109.
   4. "Se utiliza de manera correcta clases abstractas". En: ```objetos.py``` en las líneas 4, 115 y 264.
   5. "Utiliza correctamente relaciones de agregación". En: ```funciones.py``` en la función ```crear_pista()``` entre las líneas 44 y 48 se eligen el piloto y los contrincantes que deben ser agregados en la lista de corredores de la pista y se añaden al instanciarla. También varios pilotos poseen un auto, pero, como ordené los vehículos en un diccionario ordenado por los dueños no existe una relación explícita de un objeto incluyendo a otros.
   6. "Utiliza correctamente multi-herencia". En: ```objetos.py``` entre las líneas 296 y 298. Claro que también se debió adaptar los init en las pistas padres en 285 y 291.
   7. "Utiliza correctamente herencia". Similar que puntos 4 y 6.
   8. "Se  logra cargar una partida (...)". En: ```datos.py``` entre las líneas 7 y 87. Lo que hago es usar un flag para guardar el orden en que vienen los datos, luego ordenarlos según el diccionario ```Datos``` en ```parametros.py``` y finalmente instanciarlos y guardarlos en un diccionario.
   9. Todos los "Se calcula correctamente \*". En ```funciones.py``` entre las líneas 60 y 148. Las funciones tienen nombres bien explícitos.
   10. "Se gana experiencia y dinero de manera correcta según sus fórmulas". En ```funciones.py``` entre las líneas 151 y 169 se calcula la experiencia y dinero. En ```funciones.py``` en la línea 206 y 207 se le asigna al piloto lo ganado, el resto se encuentra en las properties del piloto.
   11. "Trabaja correctamente con todos los archivos CSV entregados". Similar a punto 8. Se guarda en ```datos.py``` entre las líneas 90 y 112.
   12. "Utiliza e importa correctamente parametros.py". Se utilizan parámetros en los módulos: ```datos.py```, ```menu.py``` y ```funciones.py```.
   13. "Se logran completamente las buenas prácticas indicadas". Se logran en ```funciones.py``` y ```objetos.py```.
   
   
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```math```-> ```ceil()```, ```floor()```
2. ```os```-> ```system('cls' if os.name == 'nt' else 'clear')```
3. ```random```-> ```randint()```, ```sample()```, ```random()```
4. ```abc```-> ```ABC```, ```abstractmethod```, ```abstractproperty```
5. ```collections```-> ```namedtuple```, ```defaultdict```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```main.py```-> Contine a ```main_juego()``` que va alternando los diferentes menús.
2. ```objetos.py```-> Contine todos los objetos (no menús) implementados en el juego: pilotos, vehículos, pistas y contrincantes.
3. ```datos.py```-> Hecha para el manejo de datos. Carga, guarda e instancia la información contenida en los *\.csv.
4. ```parametros.py```-> Hecha para almacenar todos los datos utilizados en el juego, incluyendo Paths y también parámetros que se usan en el flujo de menús.
5. ```funciones.py```-> Contiene todas las fórmulas que calculan valores utilizando atributos de los objetos. También incluyen otras funciones de procesado de información como ```print_final()```, y ```comprar_mejora()``` y funciones de cración de instancias nuevas como: ```crear_piloto()```, ```crear_vehiculo()``` y ```crear_pista()```.
6. ```menu.py```-> Incluye todos los menús. Los objetos contenidos aquí se encargan de la interacción con el usuario, solicitan inputs e imprimen la información necesaria.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Desde la carrera sólo se puede salir perdiendo o terminándola.
2. El usuario no se puede llamar (o a su vehículo) "" (vacio) , " " (espacio o espacios) o "0" ya que se utiliza para volver.
3. Los csv contienen datos numéricos enteros debido al enunciado. Error mio el calcular dinero y experiencia no entera por loa parámetros que inventé.
4. Lo mostrado en la consola contiene el mínimo de información que se le debía proporcionar al usuario. Características suyas o de sus vehículos deben aproximarse cualitativamente jugando varias partidas. Para corregir algunas funcionalidades será necesario usar prints que no existen en mi programa.
5. Sé que hay funciones que no debían retornar objetos porque estos "rastrean" el cambio, pero me daba más errores de los que ya tengo y traté de solucionarlo a último minuto.
6. El ```main_juego()``` es una función porque pensé que ```accion``` podría ser considerada una variable global.
7. En los pits sólo se puede comprar una mejora por vuelta.
8. Debía subir todo lo escencial y no estático (por eso los \*.csv subidos).


PD: Ahora entiendo al protagonista de Black Mirror: Bandersnatch :(.


## Referencias de código externo :book:

Para realizar mi tarea no necesité código externo.
