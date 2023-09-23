from django.db import models
from django.core.exceptions import ValidationError

# Pa validar que no sea negativo el wacho que entra equisde
def validar_numero_positivo(value):
    if value <= 0:
        raise ValidationError('El número debe ser positivo.')

# Create your models here.
class Subjects(models.Model):
    name = models.CharField(max_length=50, null= False, blank= False)
    credits = models.IntegerField(validators=[validar_numero_positivo], null=False, blank=False)