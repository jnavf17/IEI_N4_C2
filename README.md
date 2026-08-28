# IEI_N4_C2
Clases de Backend con Django

<<<<<<<<<< HEAD
## Creación Proyectos con Django

1. **Creación de repositorio en "https://github.com".**
- Vinculamos el repositorio con nuestro editor de código, idealmente VSCode.
2. **Creación de Entorno (ambiente) Virtual**
- Nos situamos en el directorio principal de nuestra aplicación.
- Ubicamos en este directorio, abrimos un terminal.
- Ejecutamos el comando:
```
python -m venv ambiente
```
- Esto crea toda la estructura de directorios necesario para nuestro proyecto y lo mantiene aislado de cualquier otro proyecto.
3. **Activación de Entorno Virtual**
- Mediante el terminal, nos ubicamos dentro del directorio del ambiente virtual. Podemos movernos con cd y cd..
- Estando en el directorio de nuestro ambiente virtual, ingresaremos al sub-directorio Scripts.
- Una vez dentro de este directorio, ejecutaremos el archivo Activate, mediante el siguiente comando:
```
.\Activate
```
- Si la ejecución del script está bloqueada por permisos de ejecución del terminal, usaremos el siguiente comando para autorizarlo:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPlicy RemoteSigned
```
- Despúes de este comando, deberíamos poder ejecutar la activación del ambiente.

4. **Actualización PIP**
- Al haber creado un nuevo proyecto, no tenemos la seguridad de tener PIP en la ultima versión, por lo que lo actualizaremos.
- Mediante terminal, ejecutaremos el siguiente comando:
```
python.exe -m pip install --upgrade pip
```
5. **Instalación de Django**
- Django depende de la última versión de pip, por lo que tuvimos que actualizarlo.
- Mediante el terminal, nos ubicamos en el directorio principal del proyecto.
- Ahora instalaremos el entorno de trabajo de Django, ejecutando el siguiente comando en el terminal:
```
pip install django
```
6. **Creamos nuestro proyecto Django**
- Creamos la estructura de directorios de Django.
- Mediante terminal, nos ubicamos en la carpeta raiz de nuestro proyecto.
- Estando en esta ubicacion, ejecutaremos el siguiente comando en el terminal:
´´´
django-admin startproject django_core .
´´´
- proyecto_django debe ser reemplazado por el nombre que ud. le dara al "motor" django, 
idealmente debe ser un nombre corto y descriptivo, porque lo vamos a llamar varias veces.
- el punto al final de la instruccion, la indica que debe crear el directorio en la carpeta raiz de nuestro proyecto

7. **Creacio de la aplicacion particular**
- Hemos llegado al punto donde construiremos nuestra aplicacion, para lograrlo debemos ubicarnos mediante terminal en la carpeta raiz del proyecto(IEI_N4_C2).
- Ejecutamos el siguiente comando mediante el terminal
´´´
django-admin startapp nombre_aplicacion
´´´
- nombre_aplicacion debe ser reemplazado por el nombre que ud. le dara a su aplicacion.

** iniciando el servidor**
- con todo instalado, ya podemos iniciar la aplicacion, para hacerlo, ejecutamos desde el terminal el comando:
´´´
python manage.py runserver
´´´