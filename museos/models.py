from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Nombre del Museo")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    # Atención: variable 'anio_fundacion'
    anio_fundacion = models.IntegerField(verbose_name="Año de Fundación")

    def __str__(self):
        return self.nombre

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200, verbose_name="Nombres y Apellidos")
    # Atención: variable 'anos_experiencia_guia'
    anos_experiencia_guia = models.IntegerField(verbose_name="Años de Experiencia")
    idiomas_hablados = models.CharField(max_length=200, help_text="Ej: Español, Inglés")
    
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='guias')

    def __str__(self):
        return self.nombre_completo

class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200, verbose_name="Título")
    duracion_meses = models.IntegerField(verbose_name="Duración (meses)")
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Producción")
    tematica = models.CharField(max_length=200, verbose_name="Temática")
    
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, verbose_name="Guía Asistente")

    def __str__(self):
        return self.titulo_exhibicion
    