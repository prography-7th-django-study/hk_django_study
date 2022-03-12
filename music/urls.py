from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# ViewSet은 Router를 통해서 하나의 url 로 처리가 가능
router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet, basename='albums')
router.register(r'songs', views.SongViewSet, basename='songs')

urlpatterns = [
    path('', include(router.urls)),
]