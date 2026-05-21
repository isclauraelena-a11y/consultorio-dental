from django.db import models
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'pacientes'

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    paciente = models.CharField(max_length=100)
    fecha_cita = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)

    class Meta:
        db_table = 'citas'