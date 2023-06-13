from django.shortcuts import render, get_object_or_404
from .models import Pokemon


def index(request):
    return render(request, 'pokedex/index.html')


def pokemon_detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon})
