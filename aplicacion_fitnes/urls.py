from django.urls import path, include
from rest_framework import routers
from aplicacion_fitnes import views

enrutador = routers.DefaultRouter()


enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)

urlpatterns = [
<<<<<<< HEAD
    path('', include(enrutador.urls))
=======
    path('', include(enrutador.urls)),
>>>>>>> e86fdaf68d467aea0af071282b7705335efeafc2
]