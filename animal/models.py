from django.db import models
from group.models import Group
from characteristic.models import Characteristic


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="animals") 
    characteristics = models.ManyToManyField(Characteristic, related_name="animals")

