from django.db import models

# Create your models here.
class paciente(models.Model):
    id_paciente=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    cc=models.CharField(max_length=40)
   
