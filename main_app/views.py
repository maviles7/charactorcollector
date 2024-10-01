from django.shortcuts import render
from .models import Character

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def character_index(request):
    characters = Character.objects.all()
    return render(request,'characters/index.html', {'characters': characters} )

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    other_names = character.other_names.split(",")
    powers = character.powers.split(",")
    return render(request, 'characters/detail.html', {'character': character, 'other_names': other_names, 'powers': powers})
