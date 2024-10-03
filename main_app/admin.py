from django.contrib import admin
from .models import Character, Name, Power

# Register your models here.

admin.site.register(Character)
admin.site.register(Name)
admin.site.register(Power)