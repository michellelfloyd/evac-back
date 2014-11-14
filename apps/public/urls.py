from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    'apps.public.views',

    url(r'^who-what/$', WhoWhat.as_view(), name='who-what-list'),
    url(r'^people/$', PersonList.as_view(), name='people-list'),
    url(r'^people/(?P<pk>[0-9]+)$', PersonDetail.as_view(), name='people-list'),
    url(r'^pet/$', PetList.as_view(), name='pets-list'),
    url(r'^pet/(?P<pk>[0-9]+)$', PetDetail.as_view(), name='pets-list'),
    url(r'^supply/$', SupplyList.as_view(), name='supply-list'),
    url(r'^supply-list/(?P<pk>[0-9]+)$', SupplyDetail.as_view(), name='supply-list'),
    url(r'^route/$', RouteList.as_view(), name='route-list'),
    url(r'^add-person/$', AddPerson.as_view(), name='people-list'),
    url(r'^add-pet/$', AddPets.as_view(), name='pets-list'),
    url(r'^special-conditions/$', SpecialConditions.as_view(), name='special-conditions'),
)
