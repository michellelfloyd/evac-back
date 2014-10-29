from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    'apps.public.views',

    url(r'^who-what/$', WhoWhat.as_view(), name='who-what-list'),
    url(r'^people/$', People.as_view(), name='people-list'),
    url(r'^people/(?P<pk>[0-9]+)$', PersonList.as_view(), name='people-list'),
    url(r'^pet/$', Pets.as_view(), name='pets-list'),
    url(r'^pets/(?P<pk>[0-9]+)$', PetList.as_view(), name='pets-list'),
    url(r'^supply/$', Supply.as_view(), name='supply-list'),
    url(r'^supply-list/(?P<pk>[0-9]+)$', SupplyList.as_view(), name='supply-list'),
    url(r'^route/$', Route.as_view(), name='route-list'),

)
