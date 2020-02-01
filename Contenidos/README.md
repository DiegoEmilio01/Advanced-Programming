# Contenidos

Los contenidos se organizan según la semana del semestre en que nos encontremos, y según la semana que se destina para su estudio. Los contenidos se subirán en paquetes de varias semanas seguidas, pero para una semana dada, solo es necesario estudiar los contenidos de dicha semana, y no las semanas posteriores incluidas en el paquete.

Los contenidos se podrán en práctica mediante actividades (formativas o sumativas), y siempre serán sobre solo uno de los contenidos semanales. La siguiente tabla muestra la correspondencia de actividades y los contenidos semanales:

|Actividad|Tipo|Semana de contenido|Contenido|
|-|-|-|-|
|AC01|Formativa|Semana 2|Programación orientada a objetos
|AC02|Sumativa|Semana 3|Estructuras de datos _built-ins_|
|AC03|Formativa|Semana 4|Iterables y funciones de orden superior|
|AC04|Formativa|Semana 5|_Threading_|
|AC05|Sumativa|Semana 6 y 7|Interfaces gráficas|
|AC06|Formativa|Semana 8|Excepciones|
|AC07|Formativa|Semana 9|Estructuras nodales parte 1|
|AC08|Formativa|Semana 10|Estructuras nodales parte 2|
|AC09|Sumativa|Semana 11|I/O y Serialización|
|AC10|Sumativa|Semana 12 y 13|_Networking_|



Si tienes dudas sobre el contenido puedes abrir una issue [aquí](https://github.com/IIC2233/Syllabus/issues).

**Importante:** Recuerda que el contenido de las actividades son acumulativas así que la materia vista en semanas anteriores también puede entrar en las actividades posteriores.

## Preguntas frecuentes

1. Yo abro los _notebooks_, hago cambios para ver como funcionan, y a la semana siguiente al hacer `git pull` me sale un error que dice "Your local changes to the following files would be overwritten by merge" ¿Qué puedo hacer?
    1. Siempre puedes clonar el repositorio otra vez, pero no es la idea. Lo que debes hacer es guardar tus cambios en alguna parte, hacer `pull`, y luego volver a aplicar tus cambios. Para eso coloca los siguientes comandos:
    
      ```bash
      git stash     # Guarda los cambios hechos en otra parte. Desaparecen del working directory.
      git pull      # El pull que queríamos hacer en un principio.
      git stash pop # Regresa los cambios hechos por ti al working directory.
      ```
