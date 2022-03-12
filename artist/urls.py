from django.urls import path, include
from .views import ArtistViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter

app_name = 'artist'

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls))
]