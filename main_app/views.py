from django.shortcuts import render, redirect
from .models import Character
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import GameSessionForm, Location



# Import HttpResponse to send text-based responses

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def character_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    gamesession_form = GameSessionForm()
    return render(request, 'characters/detail.html', {'character': character, 'gamesession_form': gamesession_form})

def add_gamesession(request, character_id):
    form = GameSessionForm(request.POST)
    if form.is_valid():
        new_gamesession = form.save(commit=False)
        new_gamesession.character_id = character_id
        new_gamesession.save()
    return redirect('character-detail', character_id=character_id)   

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['age', 'description']
    

class CharacterDelete(DeleteView):
    model = Character
    success_url='/characters/'
    
class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location
    
    
class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'challenge_level']
    
class LocationDelete(DeleteView):
    model = Location
    success_url = '/location/'