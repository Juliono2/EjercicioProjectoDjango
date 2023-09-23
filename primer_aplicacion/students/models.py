from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50, null= False, blank= False)
    lastname = models.CharField(max_length=50, null=False, blank=False)