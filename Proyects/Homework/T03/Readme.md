# Tarea 03: DCClub :school_satchel:


## Consideraciones generales :octocat:

* No tuve mucho tiempo para hacer la tarea, me concentré en hacer la parte de networking y separación fronend-backend, así que el feedback de eso es lo más me serviría para mejorar.
* Al iniciar el cliente se abren la ventana de inicio y una sala pero no alcancé a hacerla bien y no hay que prestarle atención.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Parte Networking**: Implementada parcialmente.
    * **Parte Arquitectura cliente-servidor**: Implementada parcialmente, faltó sólo implementar bien los logs del server.
    * **Parte Roles**: Implementada parcialmente, faltó distribuir los cambios en tiempo real.
* **Parte Interfaz**: Implementada parcialmente.
    * **Parte Ventana de inicio**: Implementada completamente.
    * **Parte Ventana principal**: Implementada parcialmente. El servidor le informa que las salas están vacias pero nunca se actuaizan porque no implementé poder ingresar a una.
    * **Parte Ventana principal**: Implementada parcialmente. Solo cree el objeto con dimensiones adecuadas.
* **Parte Amistades**: No implementada.
* **Parte Consultas**: No implementada.
* **Parte Archivos entregados**: Utilizados correctamente. Deben estar en la carpeta T03.
* **Parte Archivos a crear**: Utilizados correctamente. Se encuentran en las carpetas server y client.
* **Parte Bonus**: No implementados.
* **Parte .gitignore**: Implementada completamente.

* **Los ítem en amarillo de la distribución de puntajes son**:
   1. "Correcto uso de TCP/IP". En: ```client```, ```backend.py```, en el objeto ```ClienteNet``` y en ```server```, ```network.py```, en el objeto ```ServidorNet```.
   2. "Instancia y conecta los sockets de manera correcta". En los mismos objetos que el ítem anterior.
   3. "Las aplicaciones pueden trabajar concurrentemente sin bloquearse por escuchar un socket". En los mismos objetos que el primer ítem. No probé con más de un cliente pero debería funcionar. Probablemente hubiera utilizado threads para arreglar la comunicación.
   4. Roles. Implementados en los objetos ya mencionados.
   5. Codificación, decodificación e integración. En las funciones, ```listen_thread()``` y ```send()``` en el objeto ```ClienteNet``` y en las funciones ```listen_client_thread()``` y ```enviar()``` del objeto ```ServidorNet```.
   6. Existe una correcta separación entre front-end y back-end. En la tarea anterior obtuve 0 en este ítem así que ahora traté de mejorarlo, cada objeto tiene su procesador y networking aparte. En ```client``` está ```backend.py```, que contiene al procesador: ```ClienteProce``` y al objeto que maneja todo networking: ```ClienteNet``` , y ```frontend.py``` que contiene las interfaces. En ```server``` está ```network.py```, que contiene al objeto que maneja todo networking: ```ServidorNet``` y está ```procesador.py``` que contiene al procesador: ```ServidorProce```.

## Ejecución :computer:
El módulo a ejecutar es ```main.py``` en la carpeta ```server``` y después se corre cada ```main.py``` de cada cliente en la carpeta ```client```. (Deben correrse desde esas carpetas, no desde T03).


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```-> ```path.join()```
2. ```math```-> ```ceil()```
3. ```sys```.
4. ```PyQt5.QtCore``` -> ```QObject```, ```pyqtSignal```, ```QSize``` y ```Qt```.
5. ```PyQt5.QtWidgets``` -> ```QWidget```, ```QLabel```, ```QHBoxLayout```, ```QGridLayout```, ```QVBoxLayout```, ```QPushButton```, ```QLineEdit``` y ```QApplication```.
6. ```PyQt5.QtGui``` -> ```QPixmap```, ```QFont```, ```QImage```, ```QPalette```, ```QBrush``` y ```QIcon```.
7. ```json```.

### Librerías propias
Por otro lado, los módulos que fueron creados ya se describieron.

## Referencias de código externo :book:

No utilicé código externo. (Reciclé un poco de mi tarea anterior en la parte de interfaz).
