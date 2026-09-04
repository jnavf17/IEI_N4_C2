from django.http import HttpResponse
from django.shortcuts import render
def inicio(request):
    return render(request, 'aplicacion_fitnes/inicio.html')

# Create your views here.

#def inicio(request):
    #return HttpResponse('Bienvenidos a la aplicacion de fitnes')