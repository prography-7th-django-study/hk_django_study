import imp
from urllib.parse import urlparse
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# ViewSet은 Router를 통해서 하나의 url 로 처리가 가능

urlpatterns = [
  path('songs/', views.songs),
  path('songs/<int:pk>/', views.songs_detail),
]
