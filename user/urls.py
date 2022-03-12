from django.urls import path, include
from .views import PlayListViewSet, RelationshipViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register(r'playlists', PlayListViewSet, basename='playlists')
    # basename :  if you have a viewset where you've defined a custom get_queryset method, 
    #             then the viewset may not have a .queryset attribute set.
router.register(r'relationships', RelationshipViewSet, basename='relationships')
router.register(r'users', UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)), 
]