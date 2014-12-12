from models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class EvacPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvacPlan


class WhoWhatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToTake


class PeopleSerializer(serializers.ModelSerializer):

    parent = serializers.PrimaryKeyRelatedField()
    supplies = serializers.PrimaryKeyRelatedField(many=True, required=False)

    class Meta:
        depth = 2
        model = Person

    def get_supply(self, obj):
        return SupplySerializer(obj.supply.all(), many=True).data


class PeoplePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person


class PetsSerializer(serializers.ModelSerializer):

    parent = serializers.PrimaryKeyRelatedField()
    supplies = serializers.PrimaryKeyRelatedField(many=True, required=False)

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
        depth = 2
        model = Route


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop


class SpecialConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialConditions
