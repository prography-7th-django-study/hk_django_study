from django.urls import path
from .views import *

app_name = 'user'

# FBV 
urlpatterns = [
  # User
	path('users', user_list), 
	path('users/<int:pk>', user_detail),
  
  # PlayList
  path('playlists', play_list),
  path('playlist/<int:pk>', play_list_detail),
  
  # Relationship
  path('relationships', relationship),
  path('relationships/<int:pk>', relationship_detail),
  
]