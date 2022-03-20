from django.urls import path, include
from .views import PlayListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'playlist'

router = DefaultRouter()
router.register(r'playlists', PlayListViewSet, basename='playlists')

urlpatterns = [
    path('', include(router.urls)), 
]