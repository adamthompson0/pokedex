from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Ability(models.Model):
    name = models.CharField(max_length=50)
    effect = models.TextField()

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "effect": self.effect
        }


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    types = models.ManyToManyField(Type, related_name='pokemon')
    abilities = models.ManyToManyField(Ability, related_name='pokemon')

    def __str__(self):
        return self.name

    def type_to_str(self):
        return ', '.join([t.name for t in self.types.all()])

    def ability_to_str(self):
        return ', '.join([a.name for a in self.abilities.all()])

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "height": self.height,
            "weight": self.weight,
            "image_url": self.image_url,
            "types": [t.serialize() for t in self.types.all()],
            "abilities": [a.serialize() for a in self.abilities.all()]
        }


class Team(models.Model):
    name = models.CharField(max_length=40)
    pokemon = models.ManyToManyField(Pokemon, related_name='teams')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name
    