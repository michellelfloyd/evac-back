from django.shortcuts import render
from serializers import *
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse
import json

# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


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
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
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


class ObtainUserAuthToken(ObtainAuthToken):

    def post(self, request):
        # print "ObtainUserAuthToken"
        email = request.DATA['username']
        lowercase_email = email.lower()
        request.DATA['username'] = lowercase_email
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])


            user = {
                'id': serializer.object['user'].id,
                'username': serializer.object['user'].username,
                'first_name': serializer.object['user'].first_name,
                'token': token.key
            }
            # import pdb; pdb.set_trace()
            return Response(user)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def obtain_user_from_token(r, token):
    auth = TokenAuthentication()
    response = auth.authenticate_credentials(token)

    user = {
        'id': response[0].id,
        'username': response[0].username,
        'first_name': response[0].first_name,
        'token': token,
    }
    return HttpResponse(json.dumps(user))
