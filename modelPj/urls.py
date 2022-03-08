from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('user-app/', include('user.urls')),
  path('genre-app/', include('genre.urls')),
  path('artist-app/', include('artist.urls')),
  path('music-app/', include('music.urls')),
]