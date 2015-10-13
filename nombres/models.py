from django.db import models


class Padron(models.Model):
    index = models.BigIntegerField(primary_key=True)
    clase = models.IntegerField()  # This field type is a guess.
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=(('F','F'), ('M,', 'M')))
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    tercer_nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'padron'
