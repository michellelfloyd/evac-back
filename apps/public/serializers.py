from models import *
from rest_framework import serializers


class EvacPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvacPlan


class WhoWhatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToTake


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Person

    def get_supply(self, obj):
        return SupplySerializer(obj.supply.all(), many=True).data


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Pet

    def get_supply(self, obj):
        return SupplySerializer(obj.supply.all(), many=True).data


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
