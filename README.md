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

 - Este comando inicia el servidor, el que se carga en la url http://127.0.0.1:8000.

6. **Modificando la página de inicio**
    - Por defecto cuando iniciamos el servidor carga una página con información de Django, pero no es lo que debiéramos ver cuando cargamos una aplicación, por lo que cambiaremos la página de inicio.
    - Primero debemos indicarle a Django que el directorio de nuestra aplicación contiene una APP, agregamos nuestra APP a la lista INSTALLED_APPS  de *motor_django/settings.py*:
    ```
    INSTALLED_APPS = [
        # apps de django
        'nombre_aplicacion',
    ]
    ```

    - En el directorio de nuestra app creamos un subdirectorio templates, donde pondremos nuestras vistas.
    - Dentro de este subdiretorio *nombre_aplicacion/templates* creamos la vista HTML que será renderizada por el método creado anteriormente, la que llamaremos *bienvenida.html*.
    - Dentro de este archivo, pondremos el código HTML de nuestra página de bienvenida.
    - En el archivo *nombre_aplicacion/views.py* generamos el método que renderizará la vista creada:
    ```
    def bienvenida(request):
        return render(request, 'bienvenida.html')
    ```

    - Luego debemos importar las vistas desde nuestra app en *motor_django/urls.py* y llamar al método que renderizará esa vista:
    ```
    from nombre_aplicacion import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.bienvenida, name='bienvenida'),
    ]
    ```

    - Esta ruta o *PATH* recibe 4 argumentos:
        - Ruta(string): Obligatorio. Patrón URL usado para identificar la ruta indicada en la aplicación. En este caso es '', una ruta vacía, o el inicio de nuestra APP, después del nombre del servidor *http://127.0.0.1:8000/*.
        - Vista(function): Obligatorio. Función que se llamará al cargar esa URL en la aplicación, las que deberían existir en *nombre_aplicacion/views.py*. En este caso llamaremos a la función *bienvenida* que creamos en *nombre_aplicacion/views.py*.
        - Argumentos(Dictionary): Opcional. Argumentos que se enviarán a nuestra función. 
        - name(string): Opcional. Nombre que le daremos a nuestro patrón URL. En este caso lo llamaremos *'bienvenida'* y de esa forma podemos llamarlo por nombre.

    - Cuando iniciemos nuevamente nuestro servidor, debiera cargar la vista recién creada en lugar de la vista Django por defecto.

7. **Página de Error 404 Genérica**
    - Si python NO encuentra un recurso (página) solicitado, arrojará una página de error con información del servidor, lo que involucra un serio problema de seguridad. Para evitarlo, debemos cargar un página genérica de error, lo que lograremos de la siguiente forma:
        - Deshabilitamos el modo de pruebas de nuestra aplicación en *motor_django/settings.py*:
        ```
        DEBUG = False
        ```

        - Cuando el modo de pruebas se ha deshabilitado, ya no se verá la información del servidor al tratar de cargar un recurso que no existe, sino una página de Django que dice:
        ```
        Not Found
        The requested resource was not found on this server.
        ```

        - Si la aplicación NO esta corriendo en modo de prueba, implica que está en modo productivo, lo que nos debería indicar que nuestro servidor local no debería funcionar. Para resolver esto, debemos AUTORIZAR nuestro servidor local, para permitirle que funcione en modo de producción, modificando *motor_django/settings.py*:
        ```
        ALLOWED_HOSTS = ['localhost','127.0.0.1']
        ```

        - Para que se muestre una página de error creada por nosotros, debemos tener un directorio *templates* en nuestra aplicación y dentro de ese directorio un archivo *html* de nombre *404*. Django buscará en este directorio ese archivo y lo cargará al no encontrar un recurso.

8. **Modelo de Datos**
    - Django controlará la base de datos mediante migraciones, scripts de bases de datos que modificarán la estructura de datos.
    - Django maneja varias tablas de manera predeterminada para información interna, para que se creen en la DB, debemos ejecutar el comando:
    ```
    python manage.py migrate
    ```

    - Este comando aplicó una serie de migraciones nativas de Django en la base de datos, como permisos, usuarios, autorizaciones, sesiones, etc...
    - El siguiente paso es aplicar NUESTRO modelo a la base de datos. Para crear los modelos debemos modificar el archivo *nombre_aplicacion/models.py* y agregar las *clases* que hemos determinado para nuestro proyecto. Idealmente debiéramos tener un diagrama entidad-relación o uno de clases.
    - Nuestras clases se crearán heredando desde *models* de Django, para poder acceder a los ditintos tipos de datos que deberá tener como atributos.
    - Estructura de creación de una clase:
    ```
    class MiModelo(models.Model):
        atributo_1 = models.CharField(max_length=25,null=false)
        atributo_2 = models.TextField(max_length=100,null=false)
        atributo_3 = models.DateField(null=false)
        atributo_4 = models.TimeField(null=false)
        atributo_5 = models.DateTimeField(max_length=100,null=false)
        atributo_6 = models.IntegerField()
        atributo_7 = models.DecimalField()
        atributo_8 = models.FloatField()
        atributo_9 = models.EmailField()
        atributo_10 = models.BooleanField(default=true)
        atributo_11 = models.URLField(default=true)
        created_at = models.DateTimeField(default=ahora)
        updated_at = models.DateTimeField(auto_now=True)

    class MiModelo2(models.Model):
        atributo_referenciado = models.ForeignKey(MiModelo,on_delete=CASCADE)
        atributo_2 = models.CharField(max_length=100)
        created_at = models.DateTimeField(default=ahora)
        updated_at = models.DateTimeField(auto_now=True)
    ```

    - Con nuestras clases ya creadas, debemos GENERAR una nueva migracion con el comando:
    ```
    python manage.py makemigrations
    ```

    - Una vez que se ha creado nuestra nueva migración, debemos aplicarla a la base de datos, ejecutando nuevamente el comando:
    ```
    python manage.py migrate
    ```

    >Cada vez que modifiquemos el modelo de datos, crearemos una nueva migración y la aplicaremos a la base de datos para que se actualice de acuerdo a nuestro modelo.

9.  **Datos Iniciales de Aplicación**
    - Para contar con un set de datos iniciales en nuestra aplicación, primero debemos crear un directorio *fixtures* dentro de nuestra aplicación.
    - Una vez que hemos creado el directorio, crearemos archivos con la data inicial en formato *JSON*, *XML* o *YAML* con su extensión correspondiente.
    - Para insertar esa data en la base de datos, ejecutaremos el siguiente comando mediante terminal:
    ```
    python manage.py loaddata mi_archivo.extension
    ```
    
    - Si lo que se desea es respaldar todos los datos desde la base de datos en un archivo, ejecutaremos el siguiente comando mediante terminal:
    ```
    python manage.py dumpdata > mi_base_datos.json
    ```

    - Si se necesita respaldar todos los datos de nombre_aplicacion, se hará ejecutando el siguiente comando mediante terminal:
    ```
    python manage.py dumpdata nombre_aplicacion > nombre_aplicacion_data.json
    ```

    - Si se necesita respaldar los datos de un modelo particular, se hará ejecutando el siguiente comando mediante terminal:
    ```
    python manage.py dumpdata nombre_aplicacion.MiModelo > MiModelo_data.json
    ```

10. **Manejo de Base de Datos**
    Una base de datos en entornos profesionales debe controlarse con usuarios específicos con permisos otorgados explícitamente. Esto lo lograremos ejecutando los siguientes comandos en el motor de base de datos:

    * Crear una base de datos:
    ```
    CREATE DATABASE mi_base_datos;
    ```
    * Crear usuario remoto 'Usuario' con contraseña 'mi_contraseña'
    ```
    CREATE USER 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';
    ```
    * Conceder privilegios para nuestra base de datos al usuario remoto 'Usuario' (por ejemplo, 'mi_base_datos')
    ```
    GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'%';
    ```
    * Aplicar los cambios de privilegios (permisos)
    ``
    FLUSH PRIVILEGES;`
    ```

     ORM: Para comunicarnos con la DB usaremos un ORM (*Object Relational Mapping*), que se encargará de entender los objetos (por el lado del código) y los registros (por el lado de la base de datos). 

    | Código |          | Base de datos |
    | -------- | -------- | -------- |
    | Clase | <------> | Entidad |
    | objeto | <------> | registro |

    - Usaremos SqlAlchemy, el que se instalará mediante la ejecución del siguiente comando en el terminal:
    ```
    pip install SQLAlchemy mysqlclient
    ```

11. **Desacoplar Datos Sensibles**

    Ahora que ya estamos trabajando con una DB externa, debemos usar credenciales para conectarnos a esta nueva DB. Cualquier credencial o dato sensible no debería existir en código, incluyendo la *'SECRET_KEY'* de Django, por lo que debemos *DESACOPLAR* esos datos y ponerlos en un archivo de ambiente.

    - Instalamos la librería *decouple* para desacoplar los datos y posteriormente leerlos desde un archivo de ambiente. El siguiente comando será necesario para instalar la librería:
    ```
    pip install python-decouple
    ```

    - Creamos un archivo *.env* (archivo de ambiente) en el directorio principal de la aplicación o donde se encuentre su archivo *manage.py*.

    - En el archivo *.env* ponemos los datos sensibles en variables que tendrán como valor el dato. Es importante no dejar espacios entre el nombre de la variable y la asignación del valor:
    ```
    SECRET_KEY='cadena_de_caracteres_django_secret_key'
    ```

    - Donde necesitemos usar ese dato, generalmente en *setting.py*, importaremos el método *config* de la librería *decouple* para acceder a los datos almacenados en el arhvo de ambiente, de la siguiente forma:
    *settings.py*
    ```
    from decouple import config

    SECRET_KEY = config('SECRET_KEY')
    ```

    El método *config* traerá el valor de la variable almacenada en el archivo de ambiente que tenga el nombre que le pasamos al método como argumento.

    El mismo procedimiento debemos usar para procesar la información de la base de datos.

12. **Incorporar Modelo de Datos al administrador de Django**

    En el archivo *mi_aplicacion/admin.py* debemos *REGISTRAR* nuestro modelo de datos, para que el admin de django pueda procesar los datos y generar toda la estructura de *vistas* que nos permitan hacer este trabajo.
    Esto lo lograremos de la siguiente forma:
    *admin.py*
    ```
    from django.contrib import admin
    from .models import MiClase
    from .models import MiClase2

    # Register your models here.
    admin.site.register(MiClase)
    admin.site.register(MiClase2)
    ```

___   
> Para poder mantener las librerias actualizadas y estandarizadas para todo el equipo de desarrollo, crearemos un archivo de requerimientos con el siguiente comando:
```
pip freeze > requirements.txt
```

> Este archivo tendrá una lista de todas las librerías incluídas en nuestro *VENV*, la que podrá ser instalada en cualquier nuevo *VENV* ejecutando el siguiente comando:
```
pip install -r requirements.txt
```

> Cada vez que agreguemos una nueva librería actualizaremos el archivo de requerimientos con el comando *FREEZE*.