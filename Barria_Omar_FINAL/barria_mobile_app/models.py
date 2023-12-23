from django.db import models

# Create your models here.

class Inscrito(models.Model ):

  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=80)
  telefono = models.IntegerField(blank=False)
  fechaInscripcion = models.DateField(blank=False)
  institucion = models.CharField(max_length=80)  # (que deberá ir a buscar Nombre de la Institución al Modelo), 
  horaInscripcion = models.CharField(max_length=80)
  estado = models.CharField(max_length=80) #  (RESERVADO, COMPLETADA, ANULADA, NO ASISTEN) 
  observacion = models.CharField(max_length=80)