from django.shortcuts import render
from .models import Museo

def index(request):
    # PASO 1: Creamos la variable y le ponemos el nombre 'mis_museos'
    mis_museos = Museo.objects.all()
    
    # PASO 2: Preparamos el paquete. 
    # La clave 'lista_museos' es como se llamará en el HTML.
    # El valor 'mis_museos' debe coincidir EXACTAMENTE con el nombre del PASO 1.
    contexto = {
        'lista_museos': mis_museos 
    }
    
    return render(request, 'museos/index.html', contexto)