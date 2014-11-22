from django.shortcuts import render
from serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class EvacPlanList(generics.ListCreateAPIView):
    model = EvacPlan
    serializer_class = EvacPlanSerializer
    queryset = EvacPlan.objects.all()


class WhoWhat(generics.ListCreateAPIView):
    model = ToTake
    serializer_class = WhoWhatSerializer
    queryset = ToTake.objects.all()


class PersonDetail(generics.RetrieveUpdateAPIView):
    model = Person
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()


class PersonList(generics.ListCreateAPIView):
    model = Person
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()


class PersonPOST(generics.ListCreateAPIView):
    model = Person
    serializer_class = PeoplePOSTSerializer
    queryset = Person.objects.all()


class AddPerson(generics.CreateAPIView):
    model = Person
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()


class PetDetail(generics.RetrieveUpdateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class PetList(generics.ListCreateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class AddPets(generics.CreateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class PetDetail(generics.CreateAPIView):
    model = Pet
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()


class SupplyDetail(generics.RetrieveUpdateAPIView):
    model = Supply
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()


class SupplyList(generics.ListCreateAPIView):
    model = Supply
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()


class RouteList(generics.ListCreateAPIView):
    model = Route
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class StopDetail(generics.ListCreateAPIView):
    model = Stop
    serializer_class = StopSerializer
    queryset = Stop.objects.all()


class SpecialConditions(generics.ListCreateAPIView):
    model = SpecialConditions
    serializer_class = SpecialConditionsSerializer
    queryset = SpecialConditions.objects.all()

class MapRouteList(generics.ListCreateAPIView):
    model = MapRoute
    serializer_class = MapRouteSerializer
    queryset = MapRoute.objects.all()
