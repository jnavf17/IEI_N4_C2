from rest_framework import serializers

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

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('nombre', 'nacionalidad','iso_2', 'iso_3')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codigo', 'region')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('codigo', 'provincia', 'region')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('codigo', 'comuna', 'provincia')