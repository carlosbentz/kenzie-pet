from rest_framework import serializers


class CharactertisticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
