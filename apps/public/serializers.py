from models import *
from rest_framework import serializers


class EvacPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = EvacPlan


class WhoWhatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToTake


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
