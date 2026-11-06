from rest_framework import serializers

from .models import Pais, Provincia, Region, Comuna
from .models import Usuario
from .models import Entrenador
from .models import Ejercicio
from .models import Rutina
from .models import RutinaEjercicio
from .models import Progreso
from .models import ProgresoEjercicio
from .models import Auditoria
from .models import MetodoPago


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('__all__')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = ('__all__')

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('__all__')

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('__all__')

class RutinaEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaEjercicio
        fields = ('__all__')

class ProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progreso
        fields = ('__all__')    

class ProgresoEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoEjercicio
        fields = ('__all__')    

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = ('__all__')    

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ('__all__')    
