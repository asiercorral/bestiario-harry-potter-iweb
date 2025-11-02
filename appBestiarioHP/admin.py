from django.contrib import admin

# Register your models here.

from .models import Criatura, Raza, Peligro
admin.site.register(Criatura)
admin.site.register(Raza)
admin.site.register(Peligro)