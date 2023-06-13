from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pokedex.models import Pokemon, Type, Ability
import requests
import json


# returns json response of all pokemon sorted by number
def index(request) -> JsonResponse:
    pokemon = Pokemon.objects.all().order_by('number')
    data = {'pokemon': [pokemon.serialize() for pokemon in pokemon]}
    return JsonResponse(data)

# returns json response of single pokemon by id


def pokemon(request, number) -> JsonResponse:
    try:
        pokemon = Pokemon.objects.get(number=number)
        data = {'pokemon': pokemon.serialize()}
        return JsonResponse(data)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found.'}, status=404)

# returns json response of single pokemon by name


def pokemon_name(request, name) -> JsonResponse:
    try:
        pokemon = Pokemon.objects.get(name=name)
        data = {'pokemon': pokemon.serialize()}
        return JsonResponse(data)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found.'}, status=404)

# returns json response of all pokemon by keyword search


def pokemon_search(request) -> JsonResponse:
    search = request.GET.get('q')

    if not search:
        return JsonResponse({'error': 'No search term provided.'}, status=400)

    try:
        pokemon = Pokemon.objects.filter(name__icontains=search)
        data = {'pokemon': [pokemon.serialize() for pokemon in pokemon]}
        return JsonResponse(data)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found.'}, status=404)

# returns json response of all pokemon of given type


def types(request, type) -> JsonResponse:
    pokemon = Pokemon.objects.filter(
        types__name__iexact=type).order_by('number')
    data = {'pokemon': [pokemon.serialize() for pokemon in pokemon]}
    return JsonResponse(data)
