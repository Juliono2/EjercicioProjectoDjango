from django.contrib import admin
from .models import Subjects

# Register your models here.
@admin.register(Subjects)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('name', 'credit')