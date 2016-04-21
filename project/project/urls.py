from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        
# Viewsets define view behaviour
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# Routers provide an easy way to determine URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Connect API using URL routing
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^resting/', include('resting.urls', namespace='resting')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
