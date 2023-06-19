from django.contrib import admin

from .models import Pokemon, Type, Ability, Team


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_to_str', 'ability_to_str')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('pokemon',)


class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'effect')
    filter_horizontal = ('pokemon',)


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Team)
