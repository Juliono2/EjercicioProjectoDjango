from django.contrib import admin
from .models import Students

# Register your models here.
@admin.register(Students)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname')