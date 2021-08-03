from django.urls import path
from .views import AnimalView, AnimalRetrieveView

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalRetrieveView.as_view())
]