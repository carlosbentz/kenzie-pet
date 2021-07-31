from rest_framework import serializers
from animal.serializers import AnimalSerializer


class CharactertisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    animals = AnimalSerializer(many=True)
