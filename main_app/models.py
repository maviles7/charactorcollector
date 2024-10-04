from django.db import models
from django.urls import reverse

# Create your models here.

class Power(models.Model):
    power = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("power-detail", kwargs={"pk": self.id})

class Character(models.Model):
    main_identity = models.CharField(max_length=100)
    universe = models.CharField(max_length=100)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return f'{self.main_identity} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"character_id": self.id})
    
class Name(models.Model):
    alias = models.CharField(max_length=500)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alias}'
    
    
    