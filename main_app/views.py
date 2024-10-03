from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Power
from .forms import NameForm

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
    name_form = NameForm()
    return render(request, 'characters/detail.html', {'character': character, 'name_form': name_form})

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters/'

def add_name(request, character_id):
    form = NameForm(request.POST)
    if form.is_valid():
        new_name = form.save(commit=False)
        new_name.character_id = character_id
        new_name.save()
    return redirect('character-detail', character_id=character_id)

class PowerCreate(CreateView):
    model = Power
    fields = '__all__'

class PowerList(ListView):
    model = Power

class PowerDetail(DetailView):
    model = Power

class PowerUpdate(UpdateView):
    model = Power
    fields = ['power']

class PowerDelete(DeleteView):
    model = Power
    success_url = '/powers/'
