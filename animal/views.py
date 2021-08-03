from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer
from group.models import Group
from characteristic.models import Characteristic
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.shortcuts import get_object_or_404



class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        animal = Animal.objects.create(
                                name=data["name"], 
                                age=data["age"], 
                                weight=data["weight"], 
                                sex=data["sex"], 
                                group=Group.objects.create(**data["group"])
                            )
        
        for characteristic in data["characteristics"]:
            animal.characteristics.add(Characteristic.objects.create(**characteristic))

        serializer = AnimalSerializer(animal)


        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        
        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class AnimalRetrieveView(APIView):
    def get(self, request, animal_id=None):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serializer = AnimalSerializer(animal)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
