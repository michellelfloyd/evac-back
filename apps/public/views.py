from django.shortcuts import render
from serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class EvacPlan(generics.ListCreateAPIView):
    model = EvacPlan
    serializer_class = EvacPlanSerializer
    queryset = EvacPlan.objects.all()


class WhoWhat(generics.ListCreateAPIView):
    model = ToTake
    serializer_class = WhoWhatSerializer
    queryset = ToTake.objects.all()


class Person(generics.ListCreateAPIView):
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class Pet(generics.ListCreateAPIView):
    model = Pet
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


class Supply(generics.ListCreateAPIView):
    model = Supply
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()