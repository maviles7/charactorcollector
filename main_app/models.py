from django.db import models
from django.urls import reverse

# Create your models here.

class Character(models.Model):
    main_identity = models.CharField(max_length=100)
    universe = models.CharField(max_length=100)
    other_names = models.CharField(max_length=500)
    powers = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.main_identity} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"character_id": self.id})
    