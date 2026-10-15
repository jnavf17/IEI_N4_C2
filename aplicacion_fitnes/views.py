<<<<<<< HEAD
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets


from .models import Pais
from .models import Provincia
from .models import Region
from .models import Comuna
=======
from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais
from .models import Provincia
>>>>>>> e86fdaf68d467aea0af071282b7705335efeafc2
from .models import Usuario
from .models import Entrenador
from .models import Ejercicio
from .models import Rutina
from .models import RutinaEjercicio
from .models import Progreso
from .models import ProgresoEjercicio
from .models import Auditoria
from .models import MetodoPago
<<<<<<< HEAD
=======
from .models import Region
from .models import Comuna
>>>>>>> e86fdaf68d467aea0af071282b7705335efeafc2

from .serializer import PaisSerializer
from .serializer import RegionSerializer
from .serializer import ProvinciaSerializer
from .serializer import ComunaSerializer

# Create your views here.

def inicio(request):
<<<<<<< HEAD
    return render(request, 'Aplicacion_fitnes/inicio.html')
=======
    return render(request, 'aplicacion_fitnes/inicio.html')
>>>>>>> e86fdaf68d467aea0af071282b7705335efeafc2

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
<<<<<<< HEAD
    serializer_class = ComunaSerializer
    

=======
    serializer_class = ComunaSerializer
>>>>>>> e86fdaf68d467aea0af071282b7705335efeafc2
