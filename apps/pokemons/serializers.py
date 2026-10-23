from rest_framework import serializers

from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            "id",
            "name",
            "description",
            "avatar",
            "background",
            "level",
            "type",
            "health",
            "attack",
            "defense",
            "speed",
        ]
