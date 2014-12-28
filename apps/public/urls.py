from django.conf.urls import patterns, url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    'apps.public.views',


    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^evac-plan/$', EvacPlanList.as_view(), name='evac-plan-list'),
    url(r'^who-what/$', WhoWhat.as_view(), name='who-what-list'),
    url(r'^people/$', PersonList.as_view(), name='people-list'),
    url(r'^people/(?P<pk>[0-9]+)$', PersonDetail.as_view(), name='people-list'),
    url(r'^pet/$', PetList.as_view(), name='pets-list'),
    url(r'^pet/(?P<pk>[0-9]+)$', PetDetail.as_view(), name='pets-list'),
    url(r'^supply/$', SupplyList.as_view(), name='supply-list'),
    url(r'^supply-list/(?P<pk>[0-9]+)$', SupplyDetail.as_view(), name='supply-list'),
    url(r'^route/$', RouteList.as_view(), name='route-list'),
    url(r'^add-person/$', PersonPOST.as_view(), name='people-list'),
    url(r'^add-pet/$', AddPets.as_view(), name='pets-list'),
    url(r'^special-conditions/$', SpecialConditions.as_view(), name='special-conditions'),
    url(r'^pet-detail/$', PetDetail.as_view(), name='pet-detail'),
    url(r'^map-route/$', MapRouteList.as_view(), name='map-route-list'),
)
urlpatterns += patterns('',
    # url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
    url(r'^api-token-auth/', ObtainUserAuthToken.as_view()),
    url(r'^user-token/(?P<token>.+)$', obtain_user_from_token),
)

urlpatterns = format_suffix_patterns(urlpatterns)
