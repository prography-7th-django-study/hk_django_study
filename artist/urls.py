from django.urls import path
from .views import *

app_name = 'artist'

urlpatterns = [
  # Group
  path('groups', GroupPostListMixins.as_view()),
  path('groups/<int:pk>', GroupDetailMixins.as_view()),
  # Arist
  path('artists', ArtistListGenericAPIView.as_view()),
  path('artists/<int:pk>', ArtistDetailGenericAPIView.as_view()),
]