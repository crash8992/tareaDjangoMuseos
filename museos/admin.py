from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    # Coincide con anio_fundacion
    list_display = ('nombre', 'ciudad', 'anio_fundacion') 
    search_fields = ('nombre', 'ciudad')

@admin.register(GuiaMuseo)
class GuiaMuseoAdmin(admin.ModelAdmin):
    # Corregido: comilla cerrada en 'anos_experiencia_guia' y nombre 'museo' en singular
    list_display = ('nombre_completo', 'anos_experiencia_guia', 'idiomas_hablados', 'museo')
    list_filter = ('museo',)

@admin.register(Exhibicion)
class ExhibicionAdmin(admin.ModelAdmin):
    # Coincide con duracion_meses
    list_display = ('titulo_exhibicion', 'tematica', 'duracion_meses', 'costo_produccion', 'guia')
    list_filter = ('tematica',)