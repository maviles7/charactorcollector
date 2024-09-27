from django.shortcuts import render
from django.http import HttpResponse

class Character:
    def __init__(self, main_indentity, universe , other_names, powers):
        self.main_indentity = main_indentity
        self.universe = universe
        self.other_names = other_names
        self.powers = powers

characters = [
    Character('Tony Stark', 'Marvel', 'IronMan', 'genious, billionare'),
    Character('Steve Rogers', 'Marvel', 'Captain America', 'super solider'),
    Character('Logan', 'Marvel', 'Wolverine, James Howelett, Weapon X', 'mutant, admantium skeleton, regeneration'), 
    Character('Manon', 'TOG', 'Queen of the Cochrans', 'witch'), 
    Character('Percy Jackson', 'Riordanverse', 'Persues Jackson, Son of Posedion', 'sarcasm, manipulation of water, eartchquakes, talks to horses')
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def character_index(request):
    return render(request,'characters/index.html', {'characters': characters} )
