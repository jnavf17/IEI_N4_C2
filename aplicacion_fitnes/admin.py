from django.contrib import admin

# Register your models here.
from .models import Pais 
from .models import Provincia
from .models import Usuario
from .models import Entrenador
from .models import Ejercicio
from .models import Rutina
from .models import RutinaEjercicio
from .models import Progreso
from .models import ProgresoEjercicio
from .models import Auditoria
from .models import MetodoPago
from .models import Region
from .models import Comuna

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Usuario)
admin.site.register(Entrenador)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(RutinaEjercicio)
admin.site.register(Progreso)
admin.site.register(ProgresoEjercicio)
admin.site.register(Auditoria)
admin.site.register(MetodoPago)
admin.site.register(Region)
admin.site.register(Comuna)
