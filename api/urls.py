from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.index, name='index'),
    path('pokemon/<int:number>', views.pokemon, name='pokemon_number'),
    path('pokemon/<str:name>', views.pokemon_name, name='pokemon_name'),
    path('pokemon/search/', views.pokemon_search, name='pokemon_search'),
    path('types/<str:type>', views.types, name='types'),
]
