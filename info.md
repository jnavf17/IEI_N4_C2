# INTRODUCCION

el lado del servidor es la parte de una aplicacion web que se ejecuta en el servidor, procesando
solicitudes y generando respuestas.

## OBJETIVO
- Manejar la logica de negocio
- Acceder a bases de datos
- Enviar datos al cliente

Flujo cliente-servidor

1- Cliente: envia una peticion (http/https)
2- servidor: procesa la peticion, consulta datos y ejecuta logica
3- respuesta: devuelve html, json, xml, etc.

(mvc) modelo vista controlador
es una arquitectura de software que nos permite tener una organizacion adecuada de nuestro codigo


### MANIPULA

MODELO
- representa los datos
de la aplicacion y el
acceso a ellos

### ACTUALIZA

VISTA                                                                             
- presenta al usuario                                                                
los datos entregados por el modelo

### LO QUE VE                                                 
                                                                                   
USUARIO

### USA

- controlador
contiene la logica de
negocio (lo que debe
hacer el programa)
                                      
                                       ^    
### MANIPULA -------------------------------|

### LENGUAJES Y ENTORNOS

- Node.js (JavaScript) + Express -> Alto rendimiento, ideal para APIs.
- PHP + Laravel -> Desarrollo rapido.
- Python + Django -> Productividad y seguridad
- Java + Spring Boot -> Escalabilidad
- .NET C# + ASP.NET Core -> Ecosistema Micrisoft

### FUNCIONES DEL LADO DEL servidor

- Procesar formularios
- Autenticacion(acceso) y autorizacion(permisos)
- Manejo de sesiones(conjunto entre autenticacion y autorizacion) y cookies
- Integracion con bases de datos(ORM mapeo de objetos relacionales)
- Consumo de APIs externas
- Generacion dinamica de paginas 

### BASES DE DATOS EN BACKEND

- SQL: MYSQL, PostgreSQL, SQL Server
- NoSQL: MongoDB, Redis, Cassandra
- El servidor actua como puente entre las bases de datos y el cliente

### SEGURIDAD EN EL servidor

- Validacion de datos
- Cifrado de contraseñas
- Https y certificados ssl
- Prevencion de ataques: SQL inkection, XSS, CSRF

### TECNOLOGIAS DE SOPORTE

- Servidores web: Apache, Nginx
- Contenedores: Docker
- Orquestadores: Kubernetes
- Control de versiones: Git

### TENDENCIAS ACTUALES

- Serverless (AWS Lambda, Azure Functions)
- Microservicios
- GraphQL
- APIs RESTful y WebSockets

### CONCLUSION

- El backend es el corazon de una aplicacion web
- Las tecnologias del lado del servidor evolucionan constantemente
- La eleccion depende de requisitos, rendimiento y escalabilidad

PARA PROYECTO BACKEND
REQUERIMIENTOS FUNCIONALES Y NO FUNCIONALES Y MODELO DE DATOS