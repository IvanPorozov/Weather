from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# from weathersite.main.models import PlaceForWalk


# class PlaceForWalkSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PlaceForWalk
#         fields = ['img', 'name', 'description', 'priority']
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = PlaceForWalk.objects.all()
#     serializer_class = PlaceForWalkSerializer
#
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
