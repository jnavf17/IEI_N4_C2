from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView

from . import models as no
from . import serializer as ser

from .models import Pais
from .models import Provincia
from .models import Region
from .models import Comuna
from django.shortcuts import render
from rest_framework import viewsets

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

from .serializer import PaisSerializer
from .serializer import RegionSerializer
from .serializer import ProvinciaSerializer
from .serializer import ComunaSerializer

# Create your views here.

def inicio(request):
    return render(request, 'aplicacion_fitnes/inicio.html')

def error_404(request):
    return render(request, 'aplicacion_fitnes/404.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = no.Pais.objects.all()
    serializer_class = ser.PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = no.Region.objects.all()
    serializer_class = ser.RegionSerializer

class RegionListView(ListView):
    model = no.Region
    template_name = 'aplicacion_fitnes/lista_regiones.html'

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = no.Provincia.objects.all()
    serializer_class = ser.ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = no.Comuna.objects.all()
    serializer_class = ser.ComunaSerializer
    
