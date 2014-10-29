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


class People(generics.ListCreateAPIView):
    model = Person
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()


class PersonList(generics.RetrieveUpdateAPIView):
    model = Person
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()


class Pets(generics.ListCreateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class PetList(generics.RetrieveUpdateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class Supply(generics.ListCreateAPIView):
    model = Supply
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()


class SupplyList(generics.RetrieveUpdateAPIView):
    model = Supply
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()


class Route(generics.ListCreateAPIView):
    model = Route
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class Stop(generics.ListCreateAPIView):
    model = Stop
    serializer_class = StopSerializer
    queryset = Stop.objects.all()