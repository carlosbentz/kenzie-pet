from rest_framework import serializers
from characteristic.serializers import CharactertisticSerializer
from group.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    characteristics = CharactertisticSerializer(many=True)
    group = GroupSerializer()