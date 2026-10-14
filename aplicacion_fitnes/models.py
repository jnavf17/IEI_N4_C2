from django.db import models

str_habilitado = "Habilitado"
fecha_creacion = "Fecha de creación"
fecha_actualizacion = "Fecha de actualización"
str_codigo = "Código"

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField("Pais",max_length=50,null=False)
    nacionalidad = models.CharField("Nacionalidad",max_length=30,null=False)
    iso_2 = models.CharField("ISO 2",max_length=2,null=False)
    iso_3 = models.CharField("ISO 3",max_length=3,null=False)
    habilitado = models.BooleanField("Habilitado",default=True)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)

class Provincia(models.Model):
    codigo = models.CharField("Codigo",max_length=10,null=False)
    region = models.CharField("Region",max_length=50,null=False)
    habilitado = models.BooleanField("Habilitado",default=True)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)

class Usuario(models.Model):

    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    


# Herencia multi-tabla: un Entrenador ES un Usuario, con atributos adicionales
class Entrenador(models.Model):
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    certificaciones = models.CharField(max_length=200, null=True, blank=True)
    años_experiencia = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    


class Ejercicio(models.Model):
    GRUPO_MUSCULAR_CHOICES = (
        ('pecho', 'Pecho'),
        ('espalda', 'Espalda'),
        ('piernas', 'Piernas'),
        ('hombros', 'Hombros'),
        ('brazos', 'Brazos'),
        ('core', 'Core'),
        ('cardio', 'Cardio'),
        ('full_body', 'Full Body'),
    )
    EQUIPAMIENTO_CHOICES = (
        ('ninguno', 'Ninguno'),
        ('mancuernas', 'Mancuernas'),
        ('barra', 'Barra'),
        ('maquina', 'Maquina'),
        ('banda', 'Banda'),
        ('kettlebell', 'Kettlebell'),
    )

    nombre = models.CharField(max_length=100, null=False)
    grupo_muscular = models.CharField(max_length=20, null=False, choices=GRUPO_MUSCULAR_CHOICES)
    equipamiento = models.CharField(max_length=20, null=False, choices=EQUIPAMIENTO_CHOICES, default='ninguno')
    activo = models.BooleanField(default=True)


class Rutina(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('activa', 'Activa'),
        ('pausada', 'Pausada'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    )

    nombre = models.CharField(max_length=100, null=False)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='rutinas_creadas')
    atleta = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas_asignadas')
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES, default='borrador')
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    ejercicios = models.ManyToManyField(Ejercicio, through='RutinaEjercicio')


# Tabla intermedia: guarda series/repeticiones/peso de cada ejercicio DENTRO de una rutina
class RutinaEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.IntegerField(null=False, default=3)
    repeticiones = models.IntegerField(null=False, default=10)
    peso_kg = models.FloatField(null=True, blank=True)
    descanso_segundos = models.IntegerField(null=True, blank=True, default=60)


class Progreso(models.Model):
    ESTADO_CHOICES = (
        ('completa', 'Completa'),
        ('parcial', 'Parcial'),
        ('no_completada', 'No completada'),
    )

    atleta = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='progresos')
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='sesiones')
    fecha = models.DateTimeField(null=False)
    peso_corporal_kg = models.FloatField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES, default='completa')
    ejercicios = models.ManyToManyField(Ejercicio, through='ProgresoEjercicio')


# Tabla intermedia: detalle de cada ejercicio realizado DENTRO de una sesion de progreso
class ProgresoEjercicio(models.Model):
    progreso = models.ForeignKey(Progreso, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.IntegerField(null=True, blank=True)
    repeticiones = models.IntegerField(null=True, blank=True)
    peso_kg = models.FloatField(null=True, blank=True)


class Auditoria(models.Model):
    entidad = models.CharField(max_length=50, null=False)
    entidad_id = models.PositiveIntegerField(null=False)
    accion = models.CharField(max_length=50, null=False)
    estado_anterior = models.CharField(max_length=20, null=True, blank=True)
    estado_nuevo = models.CharField(max_length=20, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='acciones_auditoria')
    detalle = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)


class MetodoPago(models.Model):
    TIPO_CHOICES = (
        ('tarjeta', 'Tarjeta'),
        ('paypal', 'PayPal'),
        ('transferencia', 'Transferencia'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='metodos_pago')
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    proveedor = models.CharField(max_length=50, null=True, blank=True)
    ultimos_digitos = models.CharField(max_length=4, null=True, blank=True)
    predeterminado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Region(models.Model):
    nombre = models.CharField("Region",max_length=50,null=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='regiones')
    habilitado = models.BooleanField("Habilitado",default=True)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)

class Comuna(models.Model):
    nombre = models.CharField("Comuna",max_length=50,null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')
    habilitado = models.BooleanField("Habilitado",default=True)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)