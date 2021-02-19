# lumon-technical-challenge

A continuacion se muestran 2 carpetas que cada una contiene la resolución de los proyectos
que tendran como finalidad enviar a revisión para ganar la vacante de desarrolladorJr 
en la empresa Lumon SAS, el la primera carpeta **problems** contiene 2 archivos 
los cuales responden a los nombres de **capitalize-test.py** y **chat-test.py** y la segunda carpeta
contiene un proyecto que se ha hecho con **python y Vuejs utilizando la API Flask**. 

## Carpeta problems
Está carpeta carpeta contiene los archivos mencionados anteriormente
que serán dos ejercicios de manipulación de strings.

Para correr los archivos: 
    1. Descargar los archivos
    2. Utilizando su terminal favorita se utiliza el comando >>**python nombre_del_archivo.py" para cada
    uno de los archivos
    3. hacer respectivas pruebas.
    
## Carpeta projects

Esta carpeta contiene el proyecto, se trata de realizar un **sistema de almacenamiento de tareas** que cumplirá
con unos parametros especificos para el usuario que son: Ver listado de tareas registradas, agregar una tarea, editar una tarea existente,
marcar la tarea como terminada, agregar etiquetas y por ultimo agregar a un resposable de dicha tarea(esto se hace al actualizar la tarea).

### Datos tecnicos a tener en cuenta

Este consta de 3 etapas para su realización que fueron:
**Desarrollar el backend:** el backend se desarrolla con python ya que es el lenguaje lenguaje de alto nivel mas popular 
y permite reutilizar muchos componentes, ademas que facilita poder conectarse con una
API de interes. 

**Conectar la API** : Se utiliza flask para desarrollar la API ya que para este proyecto se quizo utilizar las tecnologías mas flexibles
a la hora de trabajar con Python y API's pequeñas, flask ha ofrecido una documentación y un paso a paso bastante intuitivo que ayudó y/o facilitó
la comunicación entre en front y el backend.

**El desarrollo del frontend:** Para el frontend se utiliza **Vuje js** ya que está mas actualizado e intuitivo ademas de que sus fucionalidades son
mucho mas intuitivas en comparación con **angular** y al igual que python, vuejs tiene una comunidad activa por si se presenta un problema tener la facilidad 
y rapidez de resolverlo(esto en terminos de productividad)

Para correr el proyecto se deben seguir los suguientes pasos:

    1. instalar flask: pip install Flask==1.1.2 Flask-Cors==3.0.10
    2. instalar vue: npm install -g @vue/cli@4.5.11
    3. $ npm install axios@0.21.1 --save
    4. $ npm install bootstrap@4.6.0 --save
    5. npm run serve
    6. $ npm install bootstrap-vue@2.21.2 --save
    7. clonar el repositorio de github del proyecto: https://github.com/Magno-12/lumon-technical-challenge.git   
    8. ejecutar flask del lado del servidor:
            8.1. ir a la carpeta server desde la terminal: $ cd server
            8.2. instalar la maquina virtual con el comando: $ python3.9 -m venv env
            8.3. activar la maquina virtual: $ source env/bin/activate
            8.4. dentro de la maquina virtual utilizar el comando: (env)$ python app.py
            
            navegar con http://localhost:5000
            
    9. ejecutar Vuejs del lado del cliente en una terminal diferente:
            9.1. ir a la carpeta client: cd client
            9.2. utilizar el comando: npm install
            9.3. correr el servidor: npm run serve 
            
            navegar con http://localhost:8080
          
