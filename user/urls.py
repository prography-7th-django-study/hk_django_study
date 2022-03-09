from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register(r'playlists', PlayListViewSet, basename='playlists')
    # basename : could not automatically determine the name from the viewset, as it does not have a `.queryset` attribute.
router.register(r'relationships', RelationshipViewSet)
router.register(r'users', UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),  
]