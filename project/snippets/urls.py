from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from rest_framework.urlpatterns import format_suffix_patterns

import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
