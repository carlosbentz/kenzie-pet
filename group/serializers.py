from rest_framework import serializers
from animal.serializers import AnimalSerializer

class GroupSerializer(serializers.Serializer):
    name = serializers.CharField()
    scientific_name = serializers.CharField()
    animals = AnimalSerializer(many=True)