from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    'apps.public.views',

    url(r'^who-what/$', WhoWhat.as_view(), name='who-what-list'),

)
