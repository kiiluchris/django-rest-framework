from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



# Connect API using URL routing
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('resting.urls')),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
